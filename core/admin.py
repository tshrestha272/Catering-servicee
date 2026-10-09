from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'event_type', 'created_at')
    list_filter = ('event_type', 'created_at')
    search_fields = ('name', 'email', 'message')
