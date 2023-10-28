from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView,DeleteView,DetailView,CreateView,UpdateView
from .models import Blog

# Create your views here.


class BlogPostListView(ListView):
    model = Blog
    template_name = 'PostList.html'


class BlogPostDetailView(DetailView):
    model = Blog
    template_name = 'PostDetail.html'

class BlogPostCreateView(CreateView):
    model = Blog
    template_name = 'PostForm.html'
    fields = ['title', 'content']
    success_url = '/posts/' 

class BlogPostUpdateView(UpdateView):
    model = Blog
    template_name = 'PostForm.html'
    fields = ['title', 'content']
    success_url = '/posts/'

class BlogPostDeleteView(DeleteView):
    model = Blog
    template_name = 'PostConform.html'
    success_url = reverse_lazy('post-list')