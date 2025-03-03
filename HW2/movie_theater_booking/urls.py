"""
URL configuration for movie_theater_booking project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import re_path, include, path
from rest_framework.routers import DefaultRouter
from bookings.views import MovieViewSet, SeatViewSet, BookingViewSet

#url configurations
router = DefaultRouter()
router.register(r'api/movies', MovieViewSet, basename='movie')
router.register(r'api/seats', SeatViewSet, basename='seat')
router.register(r'api/bookings', BookingViewSet, basename='booking')

urlpatterns = [ 
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^', include(router.urls)),
]
'''
urlpatterns = [
    path("movies/", include("bookings.urls")),
    path("seats/", include("bookings.urls")),
    path("bookings/", include("bookings.urls")),
    path('admin/', admin.site.urls)
]
'''