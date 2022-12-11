from django.urls import path
from . import views


urlpatterns = [
    path('users/profile/', views.UserView.as_view()),
    path('users/<int:pk>/subscription/', views.SubscribeView.as_view())
    # path('users/', UserView.as_view())
]