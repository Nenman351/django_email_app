from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def register(request):
    return render(request, 'register/register.html')


def greet(request):
    return HttpResponse('Successful')