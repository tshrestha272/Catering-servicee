from django.core.management.base import BaseCommand
from catering.models import GalleryItem, MenuItem, Package, Service, Testimonial


class Command(BaseCommand):
    help = 'Adds the sample content used by the Sunrise Catering demo.'

    def handle(self, *args, **options):
        services = [
            ('Wedding Catering', 'wedding-catering', 'Beautiful menus and professional service for weddings, receptions and engagement celebrations.', 1800),
            ('Birthday & Party', 'birthday-party', 'Relaxed catering for birthdays, anniversaries and private celebrations.', 1200),
            ('Corporate Catering', 'corporate-catering', 'Professional food service for meetings, conferences and office events.', 1400),
            ('Buffet Catering', 'buffet-catering', 'A generous selection of dishes presented as a complete buffet experience.', 1300),
            ('Event Catering', 'event-catering', 'Flexible food and service support for events of different sizes.', 1500),
            ('Custom Catering', 'custom-catering', 'A menu planned around your guest list, preferences and event budget.', 1600),
        ]

        for name, slug, description, price in services:
            Service.objects.update_or_create(
                slug=slug,
                defaults={'name': name, 'description': description, 'starting_price': price, 'is_active': True}
            )

        menu = [
            ('Chicken Sekuwa', 'starter', 'Char-grilled chicken with a Nepali spice marinade.', 450, 'food-party.svg'),
            ('Paneer Tikka', 'starter', 'Smoky paneer, peppers and a light spice blend.', 380, 'food-wedding.svg'),
            ('Momo Platter', 'starter', 'Steamed and fried momo selection with chutney.', 420, 'food-party.svg'),
            ('Butter Chicken', 'main', 'Creamy tomato curry with tender chicken.', 650, 'food-wedding.svg'),
            ('Paneer Butter Masala', 'main', 'Paneer cooked in a rich tomato and cashew gravy.', 560, 'food-dessert.svg'),
            ('Mixed Vegetable Curry', 'main', 'Seasonal vegetables in a lightly spiced curry.', 420, 'food-buffet.svg'),
            ('Steamed Basmati Rice', 'rice', 'Long-grain steamed rice.', 220, 'food-buffet.svg'),
            ('Jeera Rice', 'rice', 'Fragrant rice finished with cumin.', 280, 'food-buffet.svg'),
            ('Butter Naan', 'bread', 'Soft naan brushed with butter.', 180, 'food-wedding.svg'),
            ('Gulab Jamun', 'dessert', 'Warm milk dumplings in light sugar syrup.', 220, 'food-dessert.svg'),
            ('Fruit Cream', 'dessert', 'Seasonal fruit with lightly sweetened cream.', 250, 'food-dessert.svg'),
            ('Fresh Lemonade', 'drink', 'Fresh lemon, mint and chilled water.', 160, 'food-custom.svg'),
        ]

        menu_objects = []
        for name, category, description, price, image in menu:
            obj, _ = MenuItem.objects.update_or_create(
                name=name,
                defaults={'category': category, 'description': description, 'price': price, 'image': image, 'is_available': True}
            )
            menu_objects.append(obj)

        package_data = [
            ('Essential', 'A simple and delicious menu for intimate celebrations.', 1200),
            ('Premium', 'A balanced premium menu for memorable celebrations.', 1800),
            ('Royal', 'Our complete luxury catering experience for grand occasions.', 2500),
        ]
        for name, description, price in package_data:
            package, _ = Package.objects.update_or_create(
                name=name,
                defaults={'description': description, 'price_per_guest': price, 'is_active': True}
            )
            if name == 'Essential':
                package.items.set(menu_objects[:6])
            elif name == 'Premium':
                package.items.set(menu_objects[:9])
            else:
                package.items.set(menu_objects)

        gallery = [
            ('Elegant Wedding Setup', 'wedding', 'A warm and elegant table setup for a wedding celebration.', 'food-wedding.svg'),
            ('Grand Buffet Spread', 'buffet', 'A generous buffet prepared for a large family gathering.', 'food-buffet.svg'),
            ('Corporate Reception', 'corporate', 'Professional catering for a Kathmandu business event.', 'food-corporate.svg'),
            ('Dessert Table', 'dessert', 'A colourful dessert selection for guests to finish the evening.', 'food-dessert.svg'),
        ]
        for title, category, description, image in gallery:
            GalleryItem.objects.update_or_create(
                title=title,
                defaults={'category': category, 'description': description, 'image': image}
            )

        testimonials = [
            ('Priya & Suman', 'Wedding', 'The food was fresh, the staff were professional and our guests loved the whole setup.'),
            ('Ramesh K.', 'Corporate Event', 'Everything arrived on time and the team made our office event completely stress-free.'),
            ('Anita Shrestha', 'Birthday Party', 'Great food, friendly staff and a very easy booking experience.'),
        ]
        for client, event, message in testimonials:
            Testimonial.objects.update_or_create(
                client_name=client,
                defaults={'event_type': event, 'message': message, 'rating': 5, 'is_approved': True}
            )

        self.stdout.write(self.style.SUCCESS('Demo content added successfully.'))
