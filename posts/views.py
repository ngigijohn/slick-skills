
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy


from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post
from .forms import PostForm
from .filters import  PostFilter

# create your views here

def home(request):
    posts = Post.objects.all()[:5]
    return render(request, 'base/home.html',{'posts': posts})


class PostList(LoginRequiredMixin, ListView):
    paginate_by = 15
    model = Post
    context_object_name = 'posts'
    template_name = "base/post_list.html"

    def get_queryset(self):
        qs = super().get_queryset()
        my_filter = PostFilter(self.request.GET, queryset = qs )
        sorting_order = self.request.GET.get('sort-area') or ''
        print(sorting_order)
        print("Sorting. post.views_-------------------_")
        # if sorting:
        #     context['posts'] = context['posts'].filter(
        #         company_name__icontains=sorting)
        # context['sorting'] = sorting
        return my_filter.qs.order_by('-created')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = context['posts']
        

        my_filter = PostFilter(self.request.GET, queryset = self.get_queryset())

        context['my_filter'] = my_filter
        context['count'] = len(my_filter.qs)
        return context


class PostDetail(DetailView):
    model = Post
    template_name = "base/post_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["bookmarks"] = self.object.bookmarks.all() 
        return context
    


class PostCreate(LoginRequiredMixin, CreateView):
    form_class = PostForm
    success_url = reverse_lazy('posts')
    template_name = "base/post_form.html"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(PostCreate, self).form_valid(form)


class PostUpdate(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostForm
    success_url = reverse_lazy('posts')
    template_name = 'base/post_form.html'


class PostDelete(LoginRequiredMixin, DeleteView):
    model = Post
    context_object_name = 'post'
    success_url = reverse_lazy('posts')
    template_name = 'base/post_confirm_delete.html'


class BookmarkedPostList(LoginRequiredMixin, ListView):
    model = Post
    context_object_name = 'posts'
    template_name = "base/bookmarks_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = context['posts'].filter(bookmarks=self.request.user)
        return context
