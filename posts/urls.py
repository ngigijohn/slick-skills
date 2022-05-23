from django.urls import path
from .views import PostList, PostDetail, PostDelete, PostUpdate, PostCreate, CustomLoginView, RegisterPage, index
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("index/", index, name='index'),
    path("accounts/login/", CustomLoginView.as_view(), name="login"),
    path("accounts/logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("accounts/register/", RegisterPage.as_view(), name="register"),
    path('', PostList.as_view(), name='posts'),
    path('post-detail/<int:pk>/', PostDetail.as_view(), name="post-detail"),
    path("post-create/", PostCreate.as_view(), name="post-create"),
    path("post-update/<int:pk>/", PostUpdate.as_view(), name="post-update"),
    path("post-delete/<int:pk>/", PostDelete.as_view(), name="post-delete"),
    
]
