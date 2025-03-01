from rest_framework.request import Request
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.decorators import api_view
# from django.shortcuts import render

from rest_framework import viewsets, status
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer

# Create your views here.

@api_view(http_method_names=["GET", "POST"])
def bookingspage(request:Request):
    if request.method == "POST":
        data = request.data
        response = {"message": "Hello","data":data}
        return HttpResponse(data=response, status=status.HTTP_200_CREATED)
        
    response = {"message": "booking page"}
    return HttpResponse(data=response, status=status.HTTP_200_OK)


class MovieViewSet(viewsets.ViewSet):
    def list(self,request):
        queryset = Movie.objects.all()
        serializer=MovieSerializer(instance=queryset,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

    def retrieve(self,request:Request,pk=None):
        post=get_object_or_404(Post,pk=pk)
        serializer = MovieSerializer(instance=post)
        return Response(data=serializer,status=status.HTTP_200_OK)



class SeatViewSet(viewsets.ViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer


class BookingViewSet(viewsets.ViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
        