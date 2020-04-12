from django import forms
from .models import Users, Comments
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class VideoSearchForm(forms.Form):
    search = forms.CharField(max_length=100)
    
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['username', 'video', 'describe']