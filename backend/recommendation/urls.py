from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.index),
    path("genre/", views.genre),
    path("actor/", views.actor),
    path("director/", views.director),
]