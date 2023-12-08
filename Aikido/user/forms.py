from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser
from .models import Event
from django import forms

class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password1', 'password2']


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['title', 'start_time', 'end_time', 'description']