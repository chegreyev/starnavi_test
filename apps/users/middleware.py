from django.utils import timezone
from django.utils.deprecation import MiddlewareMixin
from users.models import User


class LastActivityMiddleware(MiddlewareMixin):

    def process_response(self, request, response):
        if request.user.is_authenticated:
            User.objects.filter(uuid=request.user.uuid).update(last_activity=timezone.now())
        return response
