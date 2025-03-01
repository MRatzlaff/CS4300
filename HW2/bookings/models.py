from django.db import models
from datetime import datetime

# Create your models here.
class Movie(models.Model):
    template = loader.get_template('myfirst.html')
    title = models.CharField(max_length=200, default='')
    description = models.CharField(max_length=200, default='')
    release_date = models.DateTimeField(default=datetime.now)
    duration = models.IntegerField(default=0)

    def __str__(self):
        return self.movie_title

class Seat(models.Model):
    
    seat_number = models.IntegerField(default=0)
    booking_status = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.seats


class Booking(models.Model):
    
    movie_chosen = models.CharField(max_length=200, default='')
    seat_chosen = models.CharField(max_length=10, default='')
    user = models.CharField(max_length=200, default='')
    booking_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.current_bookings
