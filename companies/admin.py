from django.contrib import admin
from .models import Companies


@admin.register(Companies)
class CompaniesAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'created_at', 'updated_at')
    list_filter = ('updated_at',)
