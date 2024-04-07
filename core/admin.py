from django.contrib import admin
from core.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
# Register your models here.

@admin.register(User)
class UserAdmin(BaseUserAdmin):
       list_display = ['id', 'username', 'email', 'is_active', 'created_at']
       add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username","first_name", "last_name", "email", "password1", "password2"),
            },
        ),
    )
    

    