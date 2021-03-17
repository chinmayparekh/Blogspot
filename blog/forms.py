from .models import Post, Comment
from django import forms

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('Name', 'Email', 'Body')