from django.urls import path
from . import views


urlpatterns = [
    path('cities/', views.cities, name='cities'),
    path('sport/', views.sport, name='sport'),
    path('groups/', views.groups, name='groups'),
    path('groupsex/', views.groupsex, name='groupsex'),
]