from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from posts.models import Post
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def add_bookmark(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.bookmarks.filter(id=request.user.id).exists():
        post.bookmarks.remove(request.user)
    else:
        post.bookmarks.add(request.user)
    return HttpResponseRedirect(request.META['HTTP_REFERER'])
