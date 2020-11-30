from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.http import HttpResponse
from .models import Post

def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'post'
    ordering = ['-date_posted'] # Упорядочивание постов по дате обнавления

class PostDetailView(DetailView):
    model = Post

def about(request):
    return render(request, 'blog/about.html', {'title': 'О блоге'})