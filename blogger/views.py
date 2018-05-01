from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Tag, Category
from .form import CommentForm

# Create your views here.


def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    tag_list = Tag.objects.all()
    category_list = Category.objects.all()
    return render(
        request,
        'blogger/index.html',
        context={
            'post_list': post_list,
            'tag_list': tag_list,
            'category_list': category_list
        })


def tmpDetail(request, pk=None):
    return render(request, 'blogger/single_new.html')


def detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comment_list = post.comment_set.filter(is_approved=True).order_by('-created_time')
    form = CommentForm()
    return render(
        request,
        'blogger/detail.html',
        context={
            'post': post,
            'form': form,
            'comment_list': comment_list
        })


def addComment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_list = post.comment_set.filter(is_approved=True).order_by('-created_time')
            context = {
                'post': post,
                'form': form,
                'comment_list': comment_list
            }
            return render(request, 'blogger/detail.html', context)

    return redirect('blogger:detail', post_id=post_id)
