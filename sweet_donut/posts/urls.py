from django.urls import path
from rest_framework import routers

from . import views
# from .views import PostUpdateView


urlpatterns = [
    path('post/<int:pk>', views.PostView.as_view()),
    path('post/<int:pk>/update/', views.FileUploadView.as_view()),
    path('posts/', views.PostsView.as_view()),
    path('posts/dropfile/<int:pk>/', views.FileDeleteView.as_view())
]