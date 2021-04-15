from rest_framework_simplejwt import views

from users.serializers import CustomTokenObtainSerializer


class CustomTokenObtainViewSet(views.TokenObtainPairView):
    serializer_class = CustomTokenObtainSerializer
