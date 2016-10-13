from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .serializers import UserSerializer
from rest_framework.request import Request
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import ListCreateAPIView, CreateAPIView
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer
from rest_framework_jwt.settings import api_settings

from .models import User
from rest_framework.permissions import AllowAny, IsAuthenticated


# Create your views here.
@csrf_exempt
def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    
    if user is not None:
        login(request, user)
        return HttpResponse("User logged in", status=200)
    else:
        return HttpResponse("Invalid user", status=401)

# @csrf_exempt
# def signup_view(request):
#     permission_classes = [AllowAny]
#     print("DATA ", Request(request).data)
#     serialized = UserSerializer(data=request.data)
#     if serialized.is_valid():
#         User.objects.create_user(
#             serialized.initial_data['email'],
#             serialized.initial_data['username'],
#             serialized.initial_data['display_name'],
#             serialized.initial_data['password']
#         )
#         return Response(serialized.data, status=201)
#         # return HttpResponse(serialized.data, status=201)
#     else:
#         return Response(serialized.error_messages, status=400)
#         # return HttpResponse(serialized.errors, status=400)

class UserCreateAPIView(CreateAPIView):
    permission_classes = [AllowAny]
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # def list(self, request):
    #     # Note the use of `get_queryset()` instead of `self.queryset`
    #     queryset = self.get_queryset()
    #     serializer = UserSerializer(queryset, many=True)
    #     return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
        print(serializer.data)
        payload = jwt_payload_handler(serializer.data)
        token = jwt_encode_handler(payload)

        return Response({"data": serializer.data, "token": token}, status=status.HTTP_201_CREATED, headers=headers)

    # def get(self, request, format=None):
    #     serializer = UserSerializer(self.queryset.all(), many=True)
    #     return Response({"users": serializer.data})

    # def post(self, request, format=None):
        

    # def perform_create(self, serializer):
    #     queryset = User.objects.filter(user=self.request.email)
    #     if queryset.exists():
    #         return Response("User already exist", status=400)
    #     serializer.save(user=self.request.email)
