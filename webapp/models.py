





# models.py

from django.contrib.auth.models import User
from django.db import models

class Event(models.Model):
    def __str__(self):
        return self.title

    title = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    date = models.DateField()
    available_seats = models.PositiveIntegerField()

class Booking(models.Model):
    def __str__(self):
        return f"{self.user.username} - {self.event.title}"

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    number_of_tickets = models.PositiveIntegerField()
    booking_date = models.DateField()
    booking_location = models.CharField(max_length=200)




