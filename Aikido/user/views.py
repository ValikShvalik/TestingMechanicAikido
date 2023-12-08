from django.shortcuts import render, redirect
from .forms import RegistrationForm
from .models import Event
from .forms import EventForm


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Перенаправление на страницу входа
    else:
        form = RegistrationForm()

    return render(request, 'user/registration.html', {'form': form})


def event_list(request):
    events = []
    return render(request, 'event/event_list.html', {'events': events})


def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = EventForm()

    return render(request, 'event/add_event.html', {'form': form})