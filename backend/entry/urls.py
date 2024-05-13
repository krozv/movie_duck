from django.urls import path
from . import views

urlpatterns = [
    path('', views.entry_main, name='entry-main'),
    path('<int:entry_pk>/', views.entry_detail, name='entry-detail'),
]
