from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import User, Profile, CreateUserRequest, CreateUserProfile
from django.contrib.auth.hashers import make_password
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import APIView
# Create your views here.

class RegisterUserView(APIView):
    @swagger_auto_schema(request_body=CreateUserRequest)
    def post(self, request):
        print("blabla",request.data)
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email')
        hash_password = make_password(password)
        user = User.objects.create(email=email, first_name=first_name, last_name=last_name, password=hash_password, username=username)

        return Response("User created!")
    

class RegisterUserProfile(APIView):
    @swagger_auto_schema(request_body=CreateUserProfile)
    def post(self, request):
        role = request.data.get('role')
        marcel = request.data.get('marcel')
        profile = Profile.objects.create(role=role, user_id=marcel)

        return Response("Profile created")