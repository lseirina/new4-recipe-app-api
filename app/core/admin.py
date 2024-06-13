"""
Django admin customization.
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from core import models


class UserAdmin(BaseUserAdmin):
    """define pages for user admin."""
    ordering = ['id']
    list_display = ['email', 'name']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': (
            'is_active',
            'is_staff',
            'is_superuser',
        )}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    readonly_fields = ['last_login']


admin.site.register(models.User, UserAdmin)
