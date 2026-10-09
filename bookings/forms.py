from django import forms
from .models import Booking
from catering.models import Package, Service


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = [
            'event_type', 'service', 'package', 'event_date',
            'event_time', 'guest_count', 'venue', 'special_request'
        ]
        widgets = {
            'event_date': forms.DateInput(attrs={'type': 'date'}),
            'event_time': forms.TimeInput(attrs={'type': 'time'}),
            'special_request': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Any food preferences or special requests?'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['service'].queryset = Service.objects.filter(is_active=True)
        self.fields['package'].queryset = Package.objects.filter(is_active=True)

    def clean_guest_count(self):
        guests = self.cleaned_data['guest_count']
        if guests < 1:
            raise forms.ValidationError('Guest count must be at least 1.')
        return guests
