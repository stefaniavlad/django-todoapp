from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver
from .models import Task
from datetime import timedelta


@receiver(post_save, sender=Task)
def create_task(sender, instance, created, **kwargs):
    if created:
        Task.objects.create(title=instance, category=instance.category, description=instance.description)
    else:
        task = Task.objects.get(title=instance, category=instance.category, description=instance.description)
        task.title = instance.title
        task.category = instance.category
        task.description = instance.description
        task.save()
        

@receiver(post_delete, sender=Task)
def delete_task(sender, instance, **kwargs):
    task = instance.title
    task.delete()

# @receiver(pre_save, sender=Task)
# def set_task_difficulty(sender, instance, **kwargs):
#     if instance.due_date and instance.create_date:
#         delta = instance.due_date - instance.create_date
#         days = delta.days

#         if days <= 1:
#             instance.difficulty = 1
#         elif days <= 3:
#             instance.difficulty = 2
#         elif days <= 5:
#             instance.difficulty = 3
#         elif days <= 10:
#             instance.difficulty = 4
#         else:
#             instance.difficulty = 5

