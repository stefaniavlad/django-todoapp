from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from .models import User, Profile, CreateUserRequest, CreateUserProfile


@staticmethod
def create_user(first_name, last_name, username, password, email):
    hash_password = make_password(password)
    user = User.objects.create(
        first_name=first_name,
        last_name=last_name,
        username=username,
        email=email,
        password=hash_password
    )
    return user