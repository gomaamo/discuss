from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse, reverse_lazy
from django.views.generic import (View, TemplateView, 
    ListView, DetailView, CreateView, UpdateView, DeleteView,)
from django.views.generic.edit import FormMixin, ModelFormMixin
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models, forms

class IndexView(ListView):
    model = models.Post
    context_object_name = "posts"
    ordering = "-date"
    template_name = "index.html"
    
    def get_queryset(self):
        query = self.request.GET.get("search", None)
        if query:
            q1 = models.Post.objects.filter(title__contains=query)
            q2 = models.Post.objects.filter(content__contains=query)
            if q1:
                self.queryset = q1
            else:
                self.queryset = q2
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.queryset is not None and self.queryset:
            context["results"] = self.queryset.order_by("-date")
        else:
            context["posts"] = models.Post.objects.order_by("-date")
        return context

class AboutView(TemplateView):
    template_name = "blog/about.html"

class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = "/login/"
    model = models.Post
    form_class = forms.PostForm
    template_name = "blog/post_form.html"
    success_url = reverse_lazy("index")

    def form_valid(self, form):
        f = form.save(commit=False)
        f.user = self.request.user
        f.save()
        return super().form_valid(form)
    
class PostDetailView(FormMixin, DetailView):
    context_object_name = "post"
    model = models.Post
    template_name = "blog/post_detail.html"
    form_class = forms.CommentForm

    def get_success_url(self):
        return reverse('detail', kwargs={'pk': self.object.id})

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        context["form"] = forms.CommentForm()
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        f = form.save(commit=False)
        f.user = self.request.user
        f.post = self.object
        f.save()
        return super(PostDetailView, self).form_valid(form)

class PostEditView(LoginRequiredMixin, UpdateView):
    login_url = "/login/"
    model = models.Post
    form_class = forms.PostForm

class PostDeleteView(LoginRequiredMixin, DeleteView):
    login_url = "/login/"
    model = models.Post
    success_url = reverse_lazy("index")

class UserDetailView(DetailView):
    context_object_name = "user"
    model = User
    template_name = "blog/user_detail.html"
   
class UserCreateView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = 'blog/signup.html'    

@login_required(login_url="/login/")
def comment_delete(request, pk):
    comment = get_object_or_404(models.Comment, pk=pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect("detail", pk=post_pk)
