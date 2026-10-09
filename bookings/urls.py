from django.urls import path
from . import views

urlpatterns = [
    path('new/', views.create_booking, name='create_booking'),
    path('mine/', views.my_bookings, name='my_bookings'),
    path('<int:booking_id>/', views.booking_detail, name='booking_detail'),
]
