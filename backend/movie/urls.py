from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_main),
    path('<int:movie_pk>/', views.movie_detail),
    path('request/', views.request),
    path('save/', views.save),
]
