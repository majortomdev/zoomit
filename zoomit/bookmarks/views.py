from rest_framework import viewsets
from .models import User, UrlObject
from .serializers import UserSerializer, UrlObjectSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UrlObjectViewSet(viewsets.ModelViewSet):
    queryset = UrlObject.objects.all()
    serializer_class = UrlObjectSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
