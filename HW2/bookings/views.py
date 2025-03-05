from rest_framework.request import Request
from rest_framework.response import Response
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

# for serializer
from rest_framework import viewsets, status, serializers
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer

# for html
from django.shortcuts import get_object_or_404
from rest_framework.renderers import TemplateHTMLRenderer

# Create your views here.
# create movie page viewset to list available movies
class MovieViewSet(viewsets.ViewSet):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'bookings/movie_list.html'

    # allows database to list contents
    def list(self, request):
        queryset = Movie.objects.all()
        serializer = MovieSerializer(queryset, many=True)

        movies = Movie.objects.all()    
        context= {'movies': movies}
        return render(request, "bookings/movie_list.html", context)


# create seats to list available seats in a specific movie
class SeatViewSet(viewsets.ViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

    # list available seats
    def list(self, request):
        queryset = Seat.objects.all()
        serializer = SeatSerializer(queryset, many=True)
        
        seats = Seat.objects.all()    
        context= {'seats': seats}
        return render(request, "bookings/seat_booking.html", context)

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

# show a user's booking history
class BookingViewSet(viewsets.ViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def list(self, request):
        queryset = Booking.objects.all()
        serializer = BookingSerializer(queryset, many=True)
        return render(request, "bookings/booking_history.html")

    def retrieve(self, request, pk=None):
        pass
        