from django.urls import path

from . import views

urlpatterns = [
    path('user/', views.UserListCreateAPIView.as_view()),
    path('user/<int:pk>', views.UserDetailAPIView.as_view()),
]
