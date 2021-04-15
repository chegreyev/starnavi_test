from rest_framework import viewsets, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework.backends import DjangoFilterBackend

from posts.models import Post, Like
from posts.filters import PostFilterSet
from posts.serializers import PostCreateSerializer, PostSerializer
from utils.const import LikeTypeChoice


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_class = PostFilterSet
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        serializer_class = PostSerializer

        if self.action in ['create', 'update', 'partial_update']:
            serializer_class = PostCreateSerializer

        return serializer_class

    @action(methods=['POST'], detail=True, url_path='like')
    def like(self, request, *args, **kwargs):
        user = self.request.user
        instance: Post = self.get_object()

        try:
            dislike = instance.likes.get(created_by=user)
            dislike.type = LikeTypeChoice.LIKE.value
            dislike.save(update_fields=['type'])
        except Like.DoesNotExist:
            like = Like.objects.create(
                created_by=user,
                type=LikeTypeChoice.LIKE.value
            )
            instance.likes.add(like)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    @action(methods=['POST'], detail=True, url_path='dislike')
    def dislike(self, request, *args, **kwargs):
        user = self.request.user
        instance: Post = self.get_object()

        try:
            like = instance.likes.get(created_by=user)
            like.type = LikeTypeChoice.DISLIKE.value
            like.save(update_fields=['type'])
        except Like.DoesNotExist:
            dislike = Like.objects.create(
                created_by=user,
                type=LikeTypeChoice.DISLIKE.value
            )
            instance.likes.add(dislike)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
