from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone

from bookings.models import Booking
from .models import Payment


@login_required
def make_payment(request, booking_id):
    booking = get_object_or_404(
        Booking,
        id=booking_id,
        customer=request.user
    )

    if request.method == 'POST':
        payment_method = request.POST.get('payment_method')
        transaction_id = request.POST.get('transaction_id', '').strip()

        if payment_method and transaction_id:
            Payment.objects.create(
                booking=booking,
                amount=booking.total_amount,
                transaction_id=transaction_id,
                status='paid',
                paid_at=timezone.now()
            )

            return redirect('payment_success', booking_id=booking.id)

    return render(
        request,
        'payments/make_payment.html',
        {
            'booking': booking,
        }
    )


@login_required
def payment_success(request, booking_id):
    booking = get_object_or_404(
        Booking,
        id=booking_id,
        customer=request.user
    )

    payment = Payment.objects.filter(
        booking=booking
    ).order_by('-created_at').first()

    return render(
        request,
        'payments/payment_success.html',
        {
            'booking': booking,
            'payment': payment,
        }
    )