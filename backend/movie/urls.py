from django.urls import path
from . import views

urlpatterns = [
    path('test-cors/', views.test_cors),
    path('', views.movie_main),
    path('<int:movie_pk>/', views.movie_detail),
    path('<int:movie_pk>/comment/', views.create_comment),
    path('<int:movie_pk>/comment/<int:comment_pk>/', views.comment),
    path('<int:movie_pk>/comment/<int:comment_pk>/<int:reply_pk>/', views.reply),
    path('boxoffice/', views.box_office),
    path('popular/', views.popular),
]
