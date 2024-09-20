





# forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Event, Booking

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'description', 'location', 'date', 'available_seats']

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['number_of_tickets', 'booking_date', 'booking_location']
        widgets = {
            'booking_date': forms.DateInput(attrs={'type': 'date'}),
            'booking_location': forms.TextInput(attrs={'placeholder': 'Enter location'}),
            'number_of_tickets': forms.NumberInput(attrs={'min': '1'})
        }

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(max_length=150)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')



