from django.urls import path
from .views import AllPosts, CreatePost, SinglePost

urlpatterns = [
    path('', AllPosts.as_view()),
    path('create', CreatePost.as_view()),
    path('<slug:slug>', SinglePost.as_view()),
]
