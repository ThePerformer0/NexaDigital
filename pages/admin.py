from django.contrib import admin
from .models import Temoignage

@admin.register(Temoignage)
class TemoignageAdmin(admin.ModelAdmin):
    list_display = ('author_name', 'company_name', 'rating', 'is_published', 'testimony_date')
    list_filter = ('is_published', 'rating')
    search_fields = ('author_name', 'content', 'company_name')
    list_editable = ('is_published',)
