from django.conf import settings
from django.db import models
from catering.models import Service, Package


class Booking(models.Model):
    EVENT_TYPES = [
        ('wedding', 'Wedding'),
        ('birthday', 'Birthday'),
        ('family', 'Family Event'),
        ('office', 'Office Event'),
        ('other', 'Other Event'),
    ]

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('preparing', 'Preparing'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    event_type = models.CharField(max_length=50, choices=EVENT_TYPES)
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, null=True, blank=True)
    package = models.ForeignKey(Package, on_delete=models.SET_NULL, null=True, blank=True)
    event_date = models.DateField()
    event_time = models.TimeField(blank=True, null=True)
    guest_count = models.PositiveIntegerField()
    venue = models.CharField(max_length=300)
    special_request = models.TextField(blank=True)
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, default='pending')
    total_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.get_full_name() or self.customer.username} - {self.event_type}"

    def calculate_total(self):
        if self.package:
            return self.package.price_per_guest * self.guest_count
        if self.service and self.service.starting_price:
            return self.service.starting_price * self.guest_count
        return 0
