import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True
    dependencies = [
        ('catering', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_type', models.CharField(choices=[('wedding', 'Wedding'), ('birthday', 'Birthday'), ('family', 'Family Event'), ('office', 'Office Event'), ('other', 'Other Event')], max_length=50)),
                ('event_date', models.DateField()),
                ('event_time', models.TimeField(blank=True, null=True)),
                ('guest_count', models.PositiveIntegerField()),
                ('venue', models.CharField(max_length=300)),
                ('special_request', models.TextField(blank=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('confirmed', 'Confirmed'), ('preparing', 'Preparing'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='pending', max_length=30)),
                ('total_amount', models.DecimalField(decimal_places=2, default=0, max_digits=12)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('package', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catering.package')),
                ('service', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='catering.service')),
            ],
        ),
    ]
