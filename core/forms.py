from django import forms
from .models import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'event_type', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Tell us a little about your event...'}),
        }
