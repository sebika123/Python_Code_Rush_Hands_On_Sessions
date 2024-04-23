
from django.db import models

class Event(models.Model):
    recipient_email = models.EmailField()
    scheduled_time = models.DateTimeField()
    message = models.TextField()
