from django.db import models
from datetime import datetime


# Create your models here.
# Movie model: title, description, release date, duration
class Movie(models.Model):
    movie_title = models.CharField(max_length=200, default='')
    description = models.CharField(max_length=200, default='')
    release_date = models.DateTimeField(default=datetime.now)
    duration = models.IntegerField(default=0)

    def __str__(self):
        return self.movie_title

# Seat model: seat number and booking status (available or not)
class Seat(models.Model):
    
    seat_number = models.IntegerField(default=0)
    booking_status = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.booking_status

# Booking model: shows user's chosen movie and seat, and the date of the movie
class Booking(models.Model):
    
    movie_chosen = models.CharField(max_length=200, default='')
    seat_chosen = models.CharField(max_length=10, default='')
    user = models.CharField(max_length=200, default='')
    booking_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.movie_chosen
