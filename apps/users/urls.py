from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView
)

from users.views import UserViewSet, CustomTokenObtainViewSet

router = DefaultRouter()
router.register('', UserViewSet, basename='users')

token_patterns = [
    path('', CustomTokenObtainViewSet.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('verify/', TokenVerifyView.as_view(), name='token_verify'),
]

urlpatterns = [
    path('analytics/', UserViewSet.as_view({'get': 'analytics'})),
    path('token/', include(token_patterns)),
    path(route='api-auth/', view=include('rest_framework.urls', namespace='rest_framework')),
]
urlpatterns += router.urls
