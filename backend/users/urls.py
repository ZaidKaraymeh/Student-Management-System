from django.urls import path
from .views import login_home

urlpatterns = [
    path("", login_home, name="management-login-home" )
]
