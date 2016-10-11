from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from .serializers import UserSerializer
from rest_framework.request import Request
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt
from rest_framework.generics import ListCreateAPIView

from .models import User
from rest_framework.permissions import AllowAny


# Create your views here.
def login_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)

    if user is not None:
        login(request, user)
        return HttpResponse("User logged in", status=200)
    else:
        return HttpResponse("Invalid user", status=401)

@csrf_exempt
def signup_view(request):
    permission_classes = (AllowAny,)
    print("DATA ", Request(request).data)
    serialized = UserSerializer(data=request.data)
    if serialized.is_valid():
        User.objects.create_user(
            serialized.initial_data['email'],
            serialized.initial_data['username'],
            serialized.initial_data['display_name'],
            serialized.initial_data['password']
        )
        return Response(serialized.data, status=201)
        # return HttpResponse(serialized.data, status=201)
    else:
        return Response(serialized.error_messages, status=400)
        # return HttpResponse(serialized.errors, status=400)

class UserCreateAPIView(ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()