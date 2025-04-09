from django.db import models
from django.contrib.auth.models import User
from rest_framework import serializers

# Create your models here.

class Profile(models.Model):
    # image = models.CharField(blank=True, null=True)
    # role = models.CharField(max_length=50, choices=[
    #     ("SM", "Scrum Master"), ("TL", "Team Lead"), ("D", "Developer"), ("QA", "Quality Assurance"), ("V", "View Only")], 
    #     default='V')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(default='@email.com')

    def __str__(self):
        return self.user.username

class CreateUserRequest(serializers.Serializer):
    email = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    password = serializers.CharField()
    username = serializers.CharField()


class CreateUserProfile(serializers.Serializer):
    role = serializers.CharField()
    marcel = serializers.CharField()
