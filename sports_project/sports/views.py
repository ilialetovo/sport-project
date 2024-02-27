from django.shortcuts import render
from .models import Sport


def index(request):
    return render(request, 'sports/index.html')


def football(request):
    return render(request, 'sports/football.html')


def volleyball(request):
    return render(request, 'sports/volleyball.html')


def ski(request):
    return render(request, 'sports/ski.html')


def swimming(request):
    return render(request, 'sports/swimming.html')


def basketball(request):
    return render(request, 'sports/basketball.html')