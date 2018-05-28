from django.shortcuts import render

from django.http import HttpResponse

from .models import Posts

def index(request):
    # return HttpResponse("Hello, world. You're at the posts index.")
    posts = Posts.objects.all()[:10]
    context = {
        'title': 'Latest Posts',
        'posts': posts
    }
    return render(request, 'posts/index.html', context)

