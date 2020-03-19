from blog.models import Post
from django.shortcuts import render
from django.utils import timezone


def post_list(request):
    posts = Post.objects.filter(created_at__lte=timezone.now()).order_by('created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})
