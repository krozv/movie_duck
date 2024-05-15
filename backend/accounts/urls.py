from django.urls import path
from . import views

urlpatterns = [
    path('', views.SignOutView.as_view(), name='account-signout'),
    # path('google/', views.GoogleLogin.as_view(), name='google_login'),
    # path('github/', views.GitHubLogin.as_view(), name='github_login'),
]
