from django.contrib import admin
from .models import GroupChat

@admin.register(GroupChat)
class GroupChatAdmin(admin.ModelAdmin):
    list_display = ('group_name', 'city', 'activity', 'chat_link')
    search_fields = ('city', 'activity', 'group_name')