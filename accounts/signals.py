from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from accounts.models import Profile
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def activate_user_automatically(sender, instance, created, **kwargs):
    if created and not instance.is_active:
        instance.is_active = True
        instance.save()

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
