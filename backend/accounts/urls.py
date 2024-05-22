from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.UserListView.as_view()),
    path('signout/', views.SignOutView.as_view(), name='account-signout'),
]
