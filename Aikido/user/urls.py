from django.urls import path
from .views import register
from .views import event_list, add_event

urlpatterns = [
    path('register/', register, name='register'),
    path('event/', event_list, name='event_list'),
    path('add_event/', add_event, name='add_event'),
]
