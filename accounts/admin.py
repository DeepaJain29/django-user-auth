from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, ActivationToken, PasswordResetToken

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['username', 'email', 'first_name', 'last_name', 'role', 'is_staff', 'is_active']
    search_fields = ['username', 'email']
    ordering = ['email']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('role',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('role',)}),
    )

# Register the custom user admin
admin.site.register(User, CustomUserAdmin)
admin.site.register(ActivationToken)
admin.site.register(PasswordResetToken)
