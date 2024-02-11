from django import forms #import the forms
from .models import Profile
from django.contrib.auth.models import User # we are gonne work with de user model
from django.contrib.auth.forms import UserCreationForm# import user creation form

#this code is to add the email in the registration
class CreateUserForm(UserCreationForm):#inherit from UserCreationForm
    email=forms.EmailField()
    class Meta:#define how we want our form to look like
        model=User#the concerned user that we imported
        fields=['username','email','password1','password2']# fields='__all__' if we want all
class UserUpdateForm(forms.ModelForm):#to create  a specific update page
    class Meta:
        model=User
        fields=['username','email']
class ProfileUpdateForm(forms.ModelForm):#to create  a specific update page for profile
    class Meta:
        model=Profile
        fields=['address','phone','image']