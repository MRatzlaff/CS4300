from rest_framework.request import Request
from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.template import loader
from django.shortcuts import render

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

    #template = loader.get_template('base.html')
    return render(request, "templates/base.html", context)

#create movie page viewset
class MovieViewSet(viewsets.ViewSet):
    def list(self,request):
        queryset = Movie.objects.all()
        serializer=MovieSerializer(instance=queryset,many=True)
        return Response(data=serializer.data,status=status.HTTP_200_OK)

        # import html template


    def create(self, request):
        pass

    def retrieve(self,request:Request,pk=None):
        post=get_object_or_404(Post,pk=pk)
        serializer = MovieSerializer(instance=post)
        return HttpResponse(template.render(context, request))

    def update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass



class SeatViewSet(viewsets.ViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass


class BookingViewSet(viewsets.ViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def list(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass
        