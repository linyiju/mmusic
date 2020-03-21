from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from blog.models import Post


def post_list(request):
    posts = Post.objects.filter(created_at__lte=timezone.now()).order_by('created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detial(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detial.html', {'post': post})
