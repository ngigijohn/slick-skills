
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
        print(qs)
        my_filter = PostFilter(self.request.GET, queryset = qs )
        print(my_filter)
        return my_filter.qs


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['posts'] = context['posts']
        context['count'] = context['posts'].count()

        my_filter = PostFilter(self.request.GET, queryset = self.get_queryset())
        # my_filter = PostFilter(self.request.GET, queryset = context['posts'] )
        # context['posts'] = my_filter.qs
        # filter by industry
        # filter by location
        # filter by type

        # order by date ascending
        # order by date descending


        context['my_filter'] = my_filter
        
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
    form_class = PostForm
    # fields = '__all__'
    # exclude= ['user','bookmarks']
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
