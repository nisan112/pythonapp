from django.contrib.auth import admin
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

from django.db import models



# Create your models here.
class CustomUserCreationForm(UserCreationForm):
    full_name = forms.CharField(max_length=100, required=True, label="Full Name")
    address = forms.CharField(max_length=255, required=True, widget=forms.Textarea(attrs={"rows": 3}), label="Address")
    age = forms.IntegerField(required=True, label="Age", min_value=0)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'full_name', 'address', 'age']

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    address = models.TextField()
    age = models.IntegerField()

    def __str__(self):
        return self.user.username

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)  # to associate posts with users

    def __str__(self):
        return self.title

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description']



