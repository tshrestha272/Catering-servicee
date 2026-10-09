from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.CharField(max_length=200, blank=True)
    starting_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        blank=True,
        null=True
    )
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class MenuItem(models.Model):
    CATEGORY_CHOICES = [
        ('starter', 'Starter'),
        ('main', 'Main Course'),
        ('rice', 'Rice'),
        ('bread', 'Bread'),
        ('dessert', 'Dessert'),
        ('drink', 'Drink'),
    ]

    name = models.CharField(max_length=200)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.CharField(max_length=200, blank=True)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Package(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price_per_guest = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    items = models.ManyToManyField(MenuItem, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class GalleryItem(models.Model):
    CATEGORY_CHOICES = [
        ('wedding', 'Weddings'),
        ('buffet', 'Buffet'),
        ('corporate', 'Corporate Receptions'),
        ('dessert', 'Dessert Tables'),
    ]

    title = models.CharField(max_length=200)
    category = models.CharField(
        max_length=50,
        choices=CATEGORY_CHOICES
    )
    description = models.TextField(blank=True)

    # Allows image upload from Django Admin
    image = models.ImageField(upload_to='gallery/')

    event_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title


class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    event_type = models.CharField(max_length=100)
    message = models.TextField()
    rating = models.PositiveIntegerField(default=5)
    image = models.CharField(max_length=200, blank=True)
    is_approved = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.client_name