from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from .models import *
from .forms import CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView, 
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)


            #Home
def home(request):
    context = {
        'projects' : Project.objects.all()
    }
    return render(request, 'blog/home.html', context)

def detailproject(request,id):
    context = {
        'projects' : Project.objects.get(id=id)
    }
    return render(request, 'blog/detail_project.html', context)




            #List
class List_ListView(ListView):
    model = Post
    template_name = 'blog/list.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class ListDetailView(DetailView):
    model = Post
    template_name = 'blog/detail_list.html'

class ListCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'blog/new_list.html'
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ListUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    template_name = 'blog/new_list.html'
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class ListDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/delete_list.html'
    success_url = '/list'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



            #Post
def post(request):
    context = {
        'posts': Baiviet.objects.all().order_by('-date')
    }
    return render(request, 'blog/post.html', context)

def detailpost(request,pk):
    post = get_object_or_404(Baiviet, pk=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST, author=request.user, post=post)
        if form.is_valid():
            form.save()
    comments = Comment.objects.filter(post=post)

    context = {
        "post": post,
        "comments": comments,
        "form":form
    }
    return render(request, 'blog/detail_post.html', context)
