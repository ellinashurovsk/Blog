from django.urls import path
from .views import PostsAPIList, PostAPICreate, PostAPIReadUpdateDelete

urlpatterns = [
    path('', PostsAPIList.as_view()),
    path('create', PostAPICreate.as_view()),
    path('<slug:slug>', PostAPIReadUpdateDelete.as_view()),
]
