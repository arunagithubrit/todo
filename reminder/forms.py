from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from reminder.models import Todos


class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["username","email","password1","password2"]
        

class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())


class TodoCreateForm(forms.ModelForm):
    class Meta:
        model=Todos
        fields=["title"]

class TodoChangeForm(forms.ModelForm):
    class Meta:
        model=Todos
        fields=["title","status"]
        

