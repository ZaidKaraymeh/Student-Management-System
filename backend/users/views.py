from django.shortcuts import render

# Create your views here.

def login_home(request):
    return render(request, "users/login_home.html")