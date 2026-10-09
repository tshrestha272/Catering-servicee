from django.contrib import admin
from .models import Booking

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('customer', 'event_type', 'event_date', 'guest_count', 'status', 'total_amount')
    list_filter = ('status', 'event_type')
    search_fields = ('customer__username', 'venue')
    list_editable = ('status',)
