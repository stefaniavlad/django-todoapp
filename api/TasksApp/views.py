from django.shortcuts import render
from . models import Task, CreateTask
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import APIView

# Create your views here.
class RegisterTask(APIView):
    @swagger_auto_schema(request_body=CreateTask)
    def post(self, request):
        category = request.data.get('category')
        title = request.data.get('title')
        description = request.data.get('description')
        create_date = request.data.get('create_date')
        update_date = request.data.get('update_date')
        due_date = request.data.get('due_date')
        status = request.data.get('status')
        task = Task.objects.create(category=category, title=title, description=description, create_date=create_date, update_date=update_date,
                                   due_date=due_date, status=status)

        return Response("Task created")