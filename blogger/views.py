from django.shortcuts import render
from .models import Post

# Create your views here.

def index(request):
    post = Post.objects.all().order_by('-created_time')[0]
    return render(request, 'blogger/index.html', context={'post': post})
