from django.shortcuts import render
from .models import Post

# Create your views here.


def post_list(request):
    posts = Post.objects.filter(published_date__isnull=False)
    context = {
        'posts': posts,
    }
    return render(request, 'blog/post_list.html', context)