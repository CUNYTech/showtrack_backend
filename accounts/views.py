from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .serializers import UserSerializer
from rest_framework.request import Request
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import ListCreateAPIView, CreateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework_jwt.settings import api_settings
from rest_framework import serializers
from rest_framework import status

from .models import User
from rest_framework.permissions import AllowAny, IsAuthenticated

class UserCreateAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            errors = []
            for error in serializer.errors:
                errors.append(error + ": " + serializer.errors[error][0])
            raise serializers.ValidationError({"error": errors})
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        user = User.objects.get(username=request.data['username'])
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        return Response({"token": token}, status=status.HTTP_201_CREATED, headers=headers)

class UserListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(APIView):
    def get(self, request, format=None):
        print(UserSerializer(request.user).data)
        test = api_settings.JWT_DECODE_HANDLER(request.auth)
        print(test)
        user = request.META.get("HTTP_AUTHORIZATION")
        return Response({"jwt": user, "auth": request.auth, "test": test})
