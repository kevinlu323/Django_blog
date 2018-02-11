from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Post, Comment

# Create your views here.

def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'blogger/index.html', context={'post_list': post_list})

def tmpDetail(request, pk=None):
    return render(request, 'blogger/single_new.html')

def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    #comment_list = Comment.objects.filter(post=post_id).order_by('-created_time')
    comment_list = post.comment_set.all().order_by('-created_time')
    return render(request, 'blogger/detail.html', context={'post': post, 'comment_list': comment_list})
