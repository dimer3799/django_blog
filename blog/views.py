from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.http import HttpResponse
from .models import Post

def home(request):
    context = {
        'post': Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'post'
    ordering = ['-date_posted'] # Упорядочивание постов по дате обнавления

class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def about(request):
    return render(request, 'blog/about.html', {'title': 'О блоге'})