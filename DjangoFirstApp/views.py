from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Posts
# Create your views here.

def index(request):
    # return HttpResponse('hello from DjangoFirstApp')
    posts = Posts.objects.all()[:10]

    context = {
        'title': 'Latest Posts',
        'posts': posts
    }

    return render(request, 'posts/index.html', context)


def details(request, id):
    post = Posts.objects.get(id=id)

    context = {
        'post': post
    }
    return render(request, 'posts/details.html', context)


def add(request):
    if (request.method == 'POST'):
        title = request.POST['title']
        body = request.POST['body']

        post = Posts(title=title, body=body)
        post.save()

        return redirect('/posts')
    else:
        return render(request, 'posts/add.html')
