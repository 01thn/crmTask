from django.contrib import admin
from .models import UserModel


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('login', 'email', 'last_login',)
    list_filter = ('login', 'last_login',)
