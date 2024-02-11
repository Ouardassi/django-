from django.db import models
import rest_framework
from django.contrib.auth.models import User# import the user from django
# Create your models here.

class Profile(models.Model):#in the admin page
    staff=models.OneToOneField(User,on_delete=models.CASCADE,null=True)# one user is to one profile, inherit from user, CASCADE means , if we delete the user, the profile will be automatically deleted
    address=models.CharField(max_length=200, null=True)
    phone=models.CharField(max_length=20,null=True)
    preference = models.TextField()
    image=models.ImageField(default='default1.png', upload_to='media')# it will be uploaded by th users by in default , it will take this 
    def __str__(self):
        return f'{self.staff.username}'#because staff is inherit of the user

class VendorProfile(models.Model):#in the admin page
    staff=models.OneToOneField(User,on_delete=models.CASCADE,null=True)# one user is to one profile, inherit from user, CASCADE means , if we delete the user, the profile will be automatically deleted
    address=models.CharField(max_length=200, null=True)
    phone=models.CharField(max_length=20,null=True)
    image=models.ImageField(default='default1.png', upload_to='media')# it will be uploaded by th users by in default , it will take this 
    def __str__(self):
        return f'{self.staff.username}'#because staff is inherit of the user
