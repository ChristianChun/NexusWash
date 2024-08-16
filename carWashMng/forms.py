# forms.py

from django import forms
from django.core.exceptions import ValidationError
from carWashMng.models import Booking
from carWashMng.models import Profile


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['service', 'customer_name', 'customer_email', 'booking_date', 'booking_time', 'additional_notes']

    def clean(self):
        cleaned_data = super().clean()
        booking_date = cleaned_data.get('booking_date')
        booking_time = cleaned_data.get('booking_time')

        if Booking.objects.filter(booking_date=booking_date, booking_time=booking_time).exists():
            raise ValidationError("There is already a booking at this date and time. Please choose a different time.")

        return cleaned_data


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'phone', 'email', 'birth_date']
