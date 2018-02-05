from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    posted_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)
    is_hidden = models.BooleanField(default=False)
    allow_comment = models.BooleanField(default=True)

    def __str__(self):
        shortTitle = self.title[:40] + "..." if len(self.title) > 40 else self.title
        return shortTitle


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    posted_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        shortContent = self.content[:40] + "..." if len(self.content) > 40 else self.content
        return shortContent
