from django.contrib import messages
from django.shortcuts import redirect, render
from catering.models import GalleryItem, MenuItem, Package, Service, Testimonial
from .forms import ContactForm


def home(request):
    context = {
        'services': Service.objects.filter(is_active=True)[:6],
        'packages': Package.objects.filter(is_active=True)[:3],
        'gallery_items': GalleryItem.objects.all()[:4],
        'testimonials': Testimonial.objects.filter(is_approved=True)[:3],
    }
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html', {'services': Service.objects.filter(is_active=True)})


def menu(request):
    return render(request, 'menu.html', {'menu_items': MenuItem.objects.filter(is_available=True)})


def packages(request):
    return render(request, 'packages.html', {'packages': Package.objects.filter(is_active=True)})


def gallery(request):
    return render(request, 'gallery.html', {'gallery_items': GalleryItem.objects.all()})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thanks! Your enquiry has been received. We will contact you soon.')
            return redirect('contact')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})
