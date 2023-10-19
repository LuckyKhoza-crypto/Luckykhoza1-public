from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from django.db import models
from .models import*

class LoginForm(forms.Form):
    username = forms.CharField(max_length=240)
    password = forms.CharField(max_length=63, widget=forms.PasswordInput)

class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ('username', 'password1', 'password2',)
        model = get_user_model() #imports the user information quickly
    
class PostImageForm(forms.ModelForm):
    class Meta:
        model = PostImage
        fields = ('name','bio', 'image')
        labels = {
            'Plant Name': '',
            'Bio': '',
            'image': '',
        }
        