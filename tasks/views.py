from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("Bienvenu à TaskFlow")
# Create your views here.
