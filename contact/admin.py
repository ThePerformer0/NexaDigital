from django.contrib import admin
from .models import MessageContact

@admin.register(MessageContact)
class MessageContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'submission_date', 'status')
    list_filter = ('status', 'submission_date')
    search_fields = ('name', 'email', 'subject', 'message')
    date_hierarchy = 'submission_date'
    readonly_fields = ('name', 'email', 'phone', 'subject', 'message', 'submission_date') 
