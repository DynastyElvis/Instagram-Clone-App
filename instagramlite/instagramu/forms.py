from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class UploadForm(forms.ModelForm):
    class Meta:
        model = Image
        exclude =['name','profile','likes']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude =['poster','image']

        labels={
          'comment' : '',   
        }
        widgets = {
           'comment' : forms.TextInput(attrs={'class': 'form-control','placeholder':'Add a comment...'}),
        }

class UserRegisterForm(UserCreationForm):
   email = forms.EmailField()

   class Meta:
        model = User
        fields = ['username','email','password1','password2']


        widgets = {
           'username' : forms.TextInput(attrs={'class': 'form-control','placeholder':'Username'}),
           'email' :forms.EmailInput(attrs={'class': 'form-control','placeholder':'Email Address'}),
           'password1' : forms.TextInput(attrs={'class': 'form-control','placeholder':'password'}),
           'password2' :forms.TextInput(attrs={'class': 'form-control','placeholder':'Confirm Password'}),
    
        }


    