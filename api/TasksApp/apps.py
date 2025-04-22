from django.apps import AppConfig


class TasksappConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "TasksApp"

    def ready(self):
        import TasksApp.signals
