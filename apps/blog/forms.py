# coding=utf-8
from django import forms
from .models import PostComment

__author__ = 'alexy'


class PostCommentForm(forms.ModelForm):
    class Meta:
        model = PostComment
        fields = '__all__'
