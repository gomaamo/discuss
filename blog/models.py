from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(max_length=2000)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="posts")
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("detail", kwargs={"pk": self.pk})

class Comment(models.Model):
    content = models.TextField(max_length=2000)
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, blank=True, null=True, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name="comments")
    date = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.content
    
    