from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    posted_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_hidden = models.BooleanField(default=False)
    allow_comment = models.BooleanField(default=True)


class PostDetail(models.Model):
    id = models.AutoField(primary_key=True)
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    sequence = models.PositiveIntegerField(default=0)
    content = models.TextField()


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField()
    post_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
