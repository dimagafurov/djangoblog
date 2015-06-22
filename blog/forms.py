__author__ = 'dima'

from django import forms
from django.forms import DateTimeField
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text', 'published_date')
