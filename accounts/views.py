from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect, render
from .forms import RegisterForm


def register(request):
    if request.user.is_authenticated:
        return redirect('profile')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Your account has been created.')
            return redirect('profile')
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})


@login_required
def profile(request):
    bookings = request.user.booking_set.select_related('package', 'service').order_by('-created_at')
    return render(request, 'accounts/profile.html', {'bookings': bookings})


class LoginView(auth_views.LoginView):
    template_name = 'accounts/login.html'
