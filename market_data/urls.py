"""Market Data urls."""
from django.urls import path

from . import views

urlpatterns = [path("", views.overview, name="index")]
