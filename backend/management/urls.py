from management.views import home
from django.urls import path

from .views import home

urlpatterns = [
    path("", home, name="management-home" )
]
