from django.urls import path
from .views import UserProfileUpdate, add_bookmark
from .views import CustomLoginView, RegisterPage
from django.contrib.auth.views import LogoutView
from .views import index, UserProfile, UserProfileCreate, UsersList, UserProfileUpdate
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path("index/", index, name='index'),
    path("accounts/login/", CustomLoginView.as_view(), name="login"),
    path("accounts/logout/", LogoutView.as_view(next_page="login"), name="logout"),
    path("accounts/register/", RegisterPage.as_view(), name="register"),
    path('add-bookmark/<int:pk>/', add_bookmark, name='add-bookmark'),
    path("users/", UsersList.as_view(), name="users"),
    path("user-profile/<int:pk>/", UserProfile.as_view(), name="user-profile"),
    path("user-profile-create/", UserProfileCreate.as_view(),
         name="user-profile-create"),
    path("user-profile-update/<int:pk>/",
         UserProfileUpdate.as_view(), name="user-profile-update"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
