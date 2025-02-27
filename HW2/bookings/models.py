from django.db import models

# Create your models here.
class Movie(models.Model):
    def __str__(self):
        return self.movie_title
    movie_title = "movie title"


class Seat(models.Model):
    def __str__(self):
        return self.seats
    seats = "seats available"


class Booking(models.Model):
    def __str__(self):
        return self.current_bookings
    current_bookings = "test bookings"
