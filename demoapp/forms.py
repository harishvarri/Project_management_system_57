from django import forms
from .models import Blog

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'description', 'image', 'author', 'email']
