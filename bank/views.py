from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# login
def login(request):
    return render(request, 'login.html')