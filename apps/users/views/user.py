import datetime
import dateutil.parser
from dateutil.relativedelta import relativedelta

from django.db.models import Count
from django.db.models.functions import TruncDay, TruncMonth, TruncYear

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny

from users.models import User
from users.serializers import (
    UserCreateSerializer, UserUpdateSerializer,
    UserShortSerializer, UserRetrieveSerializer,
)
from utils.const import LikeTypeChoice
from utils.tools import get_period_name


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        serializer_class = UserShortSerializer

        if self.action == 'register':
            serializer_class = UserCreateSerializer
        elif self.action == 'retrieve':
            serializer_class = UserRetrieveSerializer
        elif self.action in ['update', 'partial_update']:
            serializer_class = UserUpdateSerializer

        return serializer_class

    @action(methods=['POST'], detail=False, url_path='register',
            permission_classes=[AllowAny])
    def register(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)

    def analytics(self, request, *args, **kwargs):
        instance: User = self.request.user

        period_type = self.request.query_params.get('period_type', 'month')

        # Start Date
        start_date = request.query_params.get('start_date')
        try:
            start_date = dateutil.parser.parse(start_date)
        # TODO change Exception to handle right exception
        except Exception:
            epoch_year = datetime.date.today().year
            start_date = datetime.datetime(epoch_year, 1, 1)

        # End Date
        end_date = request.query_params.get('end_date')
        try:
            end_date = dateutil.parser.parse(end_date)
        # TODO change Exception to handle right exception
        except Exception:
            end_date = datetime.datetime.now()

        if period_type == 'day':
            # How many days are between two dates
            columns = (end_date - start_date).days
            likes = instance.like_set.filter(type=LikeTypeChoice.LIKE.value)\
                .annotate(period=TruncDay('updated_at'))\
                .values('period')\
                .annotate(likes=Count('uuid'))
            dislikes = instance.like_set.filter(type=LikeTypeChoice.DISLIKE.value) \
                .annotate(period=TruncDay('updated_at')) \
                .values('period') \
                .annotate(dislikes=Count('uuid'))
        elif period_type == 'month':
            # How many months are between two dates
            columns = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month) + 1
            likes = instance.like_set.filter(type=LikeTypeChoice.LIKE.value) \
                .annotate(period=TruncMonth('updated_at')) \
                .values('period') \
                .annotate(likes=Count('uuid'))
            dislikes = instance.like_set.filter(type=LikeTypeChoice.DISLIKE.value) \
                .annotate(period=TruncMonth('updated_at')) \
                .values('period') \
                .annotate(dislikes=Count('uuid'))
        elif period_type == 'year':
            # How many years are between two dates
            time_difference = relativedelta(end_date, start_date)
            columns = time_difference.years
            likes = instance.like_set.filter(type=LikeTypeChoice.LIKE.value) \
                .annotate(period=TruncYear('updated_at')) \
                .values('period') \
                .annotate(likes=Count('uuid'))
            dislikes = instance.like_set.filter(type=LikeTypeChoice.DISLIKE.value) \
                .annotate(period=TruncYear('updated_at')) \
                .values('period') \
                .annotate(dislikes=Count('uuid'))
            if columns == 0:
                columns = 1

        data = {'periods': []}

        for i in range(columns + 1):
            period_name = get_period_name(start_date, period_type, step=i)
            data['periods'].append({'period_num': i, 'period_name': period_name, 'likes': 0, 'dislikes': 0})

        for like in likes:
            like_period_name = get_period_name(like['period'], period_type)
            periods_item = next(
                item for item in data['periods'] if item["period_name"] == like_period_name)
            periods_item['likes'] = like['likes']

        for dislike in dislikes:
            dislike_period_name = get_period_name(like['period'], period_type)
            periods_item = next(
                item for item in data['periods'] if item["period_name"] == dislike_period_name)
            periods_item['dislikes'] = dislike['dislikes']
        return Response(data)
