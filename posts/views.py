from cgi import print_arguments
from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView

from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

from .models import Post
from .forms import PostForm


def index(request):
    template_name = 'base/login.html'
    return render(request, 'base/index.html')


class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('posts')


class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('posts')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('posts')
        return super(RegisterPage, self).get(*args, **kwargs)


# Create your views here.
class PostList(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = 'posts'
    template_name = "base/post_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['posts'] = context['posts']
        context['count'] = context['posts'].count()

        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['posts'] = context['posts'].filter(
                company_name__icontains=search_input)

        context['search_input'] = search_input

        return context


class PostDetail(DetailView):
    model = Post
    template_name = "base/post_detail.html"


class PostCreate(LoginRequiredMixin, CreateView):

    form_class = PostForm
    success_url = reverse_lazy('posts')
    template_name = "base/post_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PostCreate, self).form_valid(form)


class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    fields = [
        'company_name',
        'location',
        'industry',
        'specialization',
        'products_and_services',
        'contact',
        'application_requirements',
        'application_process',
        'application_deadline']
    success_url = reverse_lazy('posts')
    template_name = 'base/post_form.html'


class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    context_object_name = 'post'
    success_url = reverse_lazy('posts')
    template_name = 'base/post_confirm_delete.html'
