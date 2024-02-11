#this file is to do something based on a ctions
from django.contrib.auth.models import User
from .models import Profile#we will use this
from django.db.models.signals import post_save#
from django.dispatch import receiver

@receiver(post_save,sender=User)#based on the user , the profile will be created
def create_profile(sender,instance,created,**kwargs):
    if created:#if user is created
        Profile.objects.create(staff=instance)#the instance that we will create, the profile

@receiver(post_save,sender=User)
def save_profile(sender,instance,created,**kwargs):
    instance.profile.save()#save it