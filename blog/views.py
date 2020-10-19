from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

posts = [
    {
        'author': 'Петр Васильев',
        'title': 'Первый пост',
        'content': 'Первый пост для контента',
        'data_posted': 'Октябрь 01, 2020'
    },
    {
        'author': 'Иван Зайцев',
        'title': 'Второй пост',
        'content': 'Второй пост для контента',
        'data_posted': 'Октябрь 01, 2020'
    }

]

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'О блоге'})