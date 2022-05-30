from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from posts.models import Post
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic.edit import FormView
from django.contrib.auth.views import LoginView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy
from .models import UserProfile
from .forms import UserProfileForm

# Create your views here.


def index(request):
    template_name = 'base/login.html'
    return render(request, 'base/login.html')


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


@login_required
def add_bookmark(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.bookmarks.filter(id=request.user.id).exists():
        post.bookmarks.remove(request.user)
    else:
        post.bookmarks.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


class UsersList(LoginRequiredMixin, ListView):
    model = UserProfile
    context_object_name = 'users'
    template_name = "base/user_list.html"


class UserProfile(DetailView):
    model = UserProfile
    context_object_name = 'profile'
    template_name = "base/user_detail.html"


class UserProfileCreate(LoginRequiredMixin, CreateView):
    form_class = UserProfileForm
    success_url = reverse_lazy('users' )
    template_name = "base/user_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(UserProfileCreate, self).form_valid(form)


class UserProfileUpdate(LoginRequiredMixin, UpdateView):
    model = UserProfileForm
    fields = '__all__'
    success_url = reverse_lazy('user-profile')
    template_name = 'base/user_form.html'
