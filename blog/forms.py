from django import forms

from .models import Blog

class BlogForm(forms.ModelForm):

    class Meta:
        models = Blog
        fields = ["opinion"]