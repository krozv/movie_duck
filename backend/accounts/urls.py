from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.SignOutView.as_view(), name='account-signout'),
    # path('google/', views.GoogleLogin.as_view(), name='google_login'),
    # path('github/', views.GitHubLogin.as_view(), name='github_login'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
