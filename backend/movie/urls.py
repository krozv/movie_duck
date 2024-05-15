from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_main),
    path('<int:movie_pk>/', views.movie_detail),
    path('<int:movie_pk>/comment/', views.create_comment),
    path('<int:movie_pk>/comment/<int:comment_pk>/', views.comment),
]
