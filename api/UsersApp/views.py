from django.shortcuts import render
from rest_framework.response import Response
from .models import User, Profile, CreateUserRequest, CreateUserProfile
from django.contrib.auth.hashers import make_password
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import APIView
from .services.user_service import create_user
# Create your views here.

class RegisterUserView(APIView):
    @swagger_auto_schema(request_body=CreateUserRequest)
    def post(self, request):
        user = create_user(
            first_name=request.data.get('first_name'),
            last_name=request.data.get('last_name'),
            username=request.data.get('username'),
            password=request.data.get('password'),
            email=request.data.get('email')
        )
        return Response(f"User {user} created!")
    

class RegisterUserProfile(APIView):
    @swagger_auto_schema(request_body=CreateUserProfile)
    def post(self, request):
        role = request.data.get('role')
        user = request.data.get('user')
        profile = Profile.objects.create(role=role, user_id=user)

        return Response("Profile created")