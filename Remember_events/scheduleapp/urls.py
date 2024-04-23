from django.urls import path
from . import views

urlpatterns = [
    path('', views.remember_event, name='remember_event'),
]
