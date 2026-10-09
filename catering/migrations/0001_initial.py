from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField()),
                ('image', models.CharField(blank=True, max_length=200)),
                ('starting_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('starter', 'Starter'), ('main', 'Main Course'), ('rice', 'Rice'), ('bread', 'Bread'), ('dessert', 'Dessert'), ('drink', 'Drink')], max_length=50)),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('image', models.CharField(blank=True, max_length=200)),
                ('is_available', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Package',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('price_per_guest', models.DecimalField(decimal_places=2, max_digits=10)),
                ('is_active', models.BooleanField(default=True)),
                ('items', models.ManyToManyField(blank=True, to='catering.menuitem')),
            ],
        ),
        migrations.CreateModel(
            name='GalleryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('category', models.CharField(choices=[('wedding', 'Weddings'), ('buffet', 'Buffet'), ('corporate', 'Corporate Receptions'), ('dessert', 'Dessert Tables')], max_length=50)),
                ('description', models.TextField(blank=True)),
                ('image', models.CharField(max_length=200)),
                ('event_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client_name', models.CharField(max_length=100)),
                ('event_type', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('rating', models.PositiveIntegerField(default=5)),
                ('image', models.CharField(blank=True, max_length=200)),
                ('is_approved', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
