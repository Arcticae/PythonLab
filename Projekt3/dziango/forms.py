from django import forms
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth.forms import UserCreationForm


class ThreadForm(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ('title','content')


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('content',)


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=45, required=True )
    last_name = forms.CharField(max_length=45, required=True)
    email = forms.EmailField(max_length=100, help_text='example@something.something')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)
