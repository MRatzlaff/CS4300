from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import MovieViewSet, SeatViewSet, BookingViewSet

#url configurations
'''
router = DefaultRouter()
router.register(r'movies', MovieViewSet, basename='movie')
router.register(r'seats', SeatViewSet, basename='seat')
router.register(r'bookings', BookingViewSet, basename='booking')
'''
urlpatterns = [
    path('', views.MovieViewSet, name='booking')
    path('', views.SeatViewSet)
    path('', views.BookingViewSet)
]
