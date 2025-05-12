from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Comment, Post

User = get_user_model()

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'content']      

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'bio', 'profile_image']