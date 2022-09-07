from django.contrib import admin
from . import models


class UserAdmin(admin.ModelAdmin):
    # fields = ('username', 'password', 'email', 'first_name', 'last_name', 'is_active', 'is_superuser', 'is_staff', 'user_permissions', 'groups', )

    list_display = ('username', 'first_name', 'last_name', 'email', )
    list_filter = ('is_staff', 'is_active', )
    search_fields = ('last_name__startswith', )

    class Meta:
        ordering = ('last_name', 'first_name', 'date_joined', )

admin.site.register(models.User, UserAdmin)