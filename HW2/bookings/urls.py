from django.urls import path

from . import views

#url configurations
urlpatterns = [
    path("", views.MovieViewSet.as_view, name='booking')
]