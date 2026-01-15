from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class AdminCustomUser(UserAdmin):
    list_display = ('id', 'username', 'email', 'age', 'health_group')
    list_editable = ('health_group',)
    add_fieldsets = (
        (None,
         {'classes': ('wide',),
          'fields': ('username', 'last_name', 'email', 'password1', 'password2', 'age', 'health_group')
          }
         ),
    )
