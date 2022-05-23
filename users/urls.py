from django.urls import path
from .views import add_bookmark
urlpatterns =[
    path('add-bookmark/<int:pk>/', add_bookmark ,name='add-bookmark')
]