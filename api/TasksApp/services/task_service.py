from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from ..models import Task


@staticmethod
def create_task(category, title, description, create_date, update_date, due_date, status):
    task = Task.objects.create(
        category=category, 
        title=title, 
        description=description, 
        create_date=create_date, 
        update_date=update_date,
        due_date=due_date, status=status
        )
    return task
     