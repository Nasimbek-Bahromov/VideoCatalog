from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('detail/<int:postid>/', views.detail, name='detail'),
]