from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from .forms import BookingForm
from .models import Booking
from payments.models import Payment


@login_required
def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.customer = request.user
            booking.total_amount = booking.calculate_total()
            booking.save()
            Payment.objects.create(booking=booking, amount=booking.total_amount)
            messages.success(request, 'Your booking request has been submitted.')
            return redirect('booking_detail', booking_id=booking.id)
    else:
        form = BookingForm()

    return render(request, 'bookings/booking_form.html', {'form': form})


@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(customer=request.user).select_related('package', 'service')
    return render(request, 'bookings/my_bookings.html', {'bookings': bookings})


@login_required
def booking_detail(request, booking_id):
    booking = get_object_or_404(
        Booking.objects.select_related('package', 'service'),
        id=booking_id,
        customer=request.user
    )
    payment = booking.payment_set.order_by('-created_at').first()
    return render(request, 'bookings/booking_detail.html', {'booking': booking, 'payment': payment})
