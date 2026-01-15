from django.urls import path
from . import views

urlpatterns = [
    path('equipment/', views.equipment, name='equipment'),
    path('muscles/', views.muscles, name='muscles'),
    path('exercises/', views.exercises, name='exercises'),
    path('saving/', views.saving, name='saving'),
]