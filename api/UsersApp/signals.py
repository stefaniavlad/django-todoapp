from django.db.models.signals import pre_save, pre_delete, post_save, post_delete
from django.dispatch import receiver
from .models import User, Profile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, email=instance.email)
    else:
        profile = Profile.objects.get(user=instance)
        profile.email = instance.email
        profile.save()

@receiver(post_delete, sender=Profile)
def delete_user_profile(sender, instance, **kwargs):
    user = instance.user
    user.delete()

@receiver(post_save, sender=Profile)
def update_profile_user(sender, instance, created, **kwargs):
    if not created and instance.email != instance.user.email:
        user = instance.user
        user.email = instance.email
        user.save()