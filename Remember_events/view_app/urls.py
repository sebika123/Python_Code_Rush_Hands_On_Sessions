from django.urls import path
from .views import all_events, delete_event

urlpatterns = [
    path('', all_events, name='all_events'),
    path('delete/<int:event_id>/', delete_event, name='delete_event')
]
