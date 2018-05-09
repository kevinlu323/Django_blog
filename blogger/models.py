from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Tag(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    abstract = models.CharField(max_length=500, blank=True)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)
    tags = models.ManyToManyField(Tag, blank=True)
    is_hidden = models.BooleanField(default=False)
    allow_comment = models.BooleanField(default=True)

    def __str__(self):
        shortTitle = self.title[:40] + "..." if len(self.title) > 40 else self.title
        return shortTitle


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # author = models.ForeignKey(User, on_delete=models.CASCADE)
    author = models.CharField(max_length=20)
    content = models.TextField()
    created_time = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        shortContent = self.content[:40] + "..." if len(self.content) > 40 else self.content
        return shortContent
