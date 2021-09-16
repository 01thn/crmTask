from django.contrib import admin
from .models import Skills


@admin.register(Skills)
class SkillsAdmin(admin.ModelAdmin):
    # list_display = ('knowledge', 'created_at', 'updated_at')
    list_filter = ('updated_at',)