from django.urls import path
from . import views

urlpatterns = [
    path ('program/', views.programms, name='program'),
    path ('exer/', views.exer, name='exer'),
]