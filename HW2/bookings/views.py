from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.request import Request
from .models import Movie
# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the bookings page.")
class MovieViewSet(viewsets.ViewSet):
    def list(self,request:Request):
        queryset=Movie.objects.all()
        