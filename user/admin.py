from django.contrib.auth.admin import UserAdmin
from .models import User
from django.contrib import admin


class CustomUserAdmin(UserAdmin):
    # Customize fieldsets to remove username and replace it with email
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name',)}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Update the form when adding a new user in the admin
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2',),
        }),
    )

    # Display email instead of username in the user list
    list_display = ('email', 'first_name', 'last_name', 'is_staff')

    # Use email for searching
    search_fields = ('email', 'first_name', 'last_name')

    # Order by email
    ordering = ('email',)


admin.site.register(User, CustomUserAdmin)
