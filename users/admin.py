from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User


class UserAdminCustom(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'type')}),)

    list_display = ('username', 'email', 'is_superuser',
                    'is_staff', 'is_active', 'type')


admin.site.register(User, UserAdminCustom)
