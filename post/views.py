from re import template
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView
from .models import Post, Comment
from .forms import PostForm, CommentForm


class PostCreateView(CreateView):
    form_class = PostForm
    template_name = 'post_form.html'
    success_url = reverse_lazy('post_list')


class PostListView(ListView):
    model = Post
    template_name = 'post_list.html'

class PostDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context['comments'] = Comment.objects.filter(post=self.get_object())
        return context

class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post_form.html'


class CommentCreateView(CreateView):
    form_class = CommentForm
    template_name = 'comment_form.html'
    success_url = reverse_lazy('post_list')


