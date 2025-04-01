from django.db import models

# Create your models here.
class Task(models.Model):
    category = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    create_date = models.DateTimeField(auto_now=True)
    update_date = models.DateTimeField(auto_now=True)
    due_date = models.DateTimeField()
    status = models.CharField(
        max_length=20,
        choices=[("O", "Open"), ("P", "Pending"), ("C", "Completed"), ("IP", "In Progress")],
        default="Open"
    )


    def __str__(self):
        return self.title