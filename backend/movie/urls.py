from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_main),
    path('<int:movie_pk>/', views.movie_detail),
    path('<int:movie_pk>/comment/', views.create_comment),
    path('<int:movie_pk>/comments/', views.comment_list),  # commentlist 출력
    path('<int:movie_pk>/comment/<int:comment_pk>/', views.comment),
    path('<int:movie_pk>/comment/<int:comment_pk>/<int:reply_pk>/', views.reply),
    path('boxoffice/', views.box_office),
    path('<int:movie_pk>/keywords/', views.movie_keywords), # keywords 추출 views
]
