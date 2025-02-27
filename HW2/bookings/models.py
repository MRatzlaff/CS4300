from django.db import models

# Create your models here.
class Movie(models.Model):
    def __str__(self):
        return self.movie_title
    title = "movie title"
    description = "description"
    release_date = models.DateTimeField("release date")
    duration = models.IntegerField(default=0)


class Seat(models.Model):
    def __str__(self):
        return self.seats
    seat_number = models.IntegerField(default=0)
    booking_status = models.CharField(max_length=50)


class Booking(models.Model):
    def __str__(self):
        return self.current_bookings
    movie_chosen = models.CharField("movie", max_length=200)
    seat_chosen = models.CharField("seat", max_length=10)
    user = models.CharField("user", max_length=200)
    booking_date = models.DateTimeField("date of movie", default=0)
