from django import forms
from . import models

class PostForm(forms.ModelForm):
    class Meta():
        model = models.Post
        fields = ("title", "content")

        widgets = {
            "title": forms.TextInput(attrs={
                "class": "form-control",
                "placeholder": "Title"
            }),
            "content": forms.Textarea(attrs={
                "class": "form-control",
                "rows": "5",
                "placeholder": "The mike is yours :)"
            }),
        }

class CommentForm(forms.ModelForm):
    class Meta():
        model = models.Comment
        fields = ("content",)

        widgets = {
            'content': forms.Textarea(attrs={
                "class": "form-control",
                "rows": "2",
                "cols": "65",
                "placeholder": "Write a comment",
            }),
        }