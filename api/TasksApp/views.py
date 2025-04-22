from django.shortcuts import render
from . models import Task, CreateTask
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from rest_framework.decorators import APIView
from .services.task_service import create_task

class RegisterTask(APIView):
    @swagger_auto_schema(request_body=CreateTask)
    def post(self, request):
        task = create_task(
            category=request.data.get('category'), 
            title=request.data.get('title'), 
            description=request.data.get('description'), 
            create_date=request.data.get('create_date'), 
            update_date=request.data.get('update_date'),
            due_date=request.data.get('due_date'), 
            status=request.data.get('status')
        )

        return Response(f"Task {task} created")