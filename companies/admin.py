from django.contrib import admin
from .models import Companies


@admin.register(Companies)
class CompaniesAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'createdAt', 'updatedAt')
    list_filter = ('createdAt',)
