from django.contrib import admin
from .models import GalleryItem, MenuItem, Package, Service, Testimonial

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'starting_price', 'is_active')
    list_filter = ('is_active',)
    prepopulated_fields = {'slug': ('name',)}

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'is_available')
    list_filter = ('category', 'is_available')

@admin.register(Package)
class PackageAdmin(admin.ModelAdmin):
    list_display = ('name', 'price_per_guest', 'is_active')
    list_filter = ('is_active',)

@admin.register(GalleryItem)
class GalleryItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'event_date')
    list_filter = ('category',)

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'event_type', 'rating', 'is_approved')
    list_filter = ('is_approved', 'rating')
