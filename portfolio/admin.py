from django.contrib import admin
from .models import Realisation

@admin.register(Realisation)
class RealisationAdmin(admin.ModelAdmin):
    list_display = ('title', 'client_name', 'service_category', 'realization_date')
    list_filter = ('service_category', 'realization_date')
    search_fields = ('title', 'description', 'client_name')
    date_hierarchy = 'realization_date'
