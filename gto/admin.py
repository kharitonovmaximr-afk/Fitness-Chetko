from django.contrib import admin
from .models import GTONormativ

@admin.register(GTONormativ)
class GTONormativAdmin(admin.ModelAdmin):
    list_display = ['gender', 'medal', 'age_group']
    list_filter = ['gender', 'medal']