from django.db import models

# Create your models here.

class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    avatar = models.CharField(max_length=100)
    is_admin = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now=True)

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    summary = models.CharField(max_length=100)
    posted_date = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
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
    owner = models.ForeignKey(User, on_delete=models.CASCADE)




