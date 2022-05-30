from django.urls import path
from .views import PostList, PostDetail, PostDelete, PostUpdate, PostCreate, BookmarkedPostList,home


urlpatterns = [
    path('', home, name='home'),
    path('posts', PostList.as_view(), name='posts'),
    path('bookmarks/', BookmarkedPostList.as_view(), name='bookmarks'),
    path('post-detail/<int:pk>/', PostDetail.as_view(), name="post-detail"),
    path("post-create/", PostCreate.as_view(), name="post-create"),
    path("post-update/<int:pk>/", PostUpdate.as_view(), name="post-update"),
    path("post-delete/<int:pk>/", PostDelete.as_view(), name="post-delete"),

]
