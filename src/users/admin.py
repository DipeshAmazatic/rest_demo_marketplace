"""
User Admin models
"""
from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    """
    User Admin
    """
    model = User
    list_display = ('pk','email',)
    fieldsets = (
        (None, {"fields": ("password",)}),
        (_("Personal info"), {"fields": ("name", "email",'phone_no','is_email_verified')}),
        ( _("Permissions"),{"fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None,{'fields':('name','phone_no','is_email_verified',)}),
    )

admin.site.register(User, UserAdmin)
