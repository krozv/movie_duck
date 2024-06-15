from django.urls import path
from . import views

urlpatterns = [
    path('', views.UserListView.as_view()),
    path('signout/', views.SignOutView.as_view(),),
    path('profile/<int:user_pk>/', views.UserProfileview.as_view()),
]
