from django.shortcuts import render
from hotels.models import Hotel


def home(request):
    hotels = Hotel.objects.all()

    return render(request, 'home.html', {
        'hotels': hotels
    })
