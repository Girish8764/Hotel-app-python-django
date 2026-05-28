from django.shortcuts import render, redirect, get_object_or_404

from .forms import BookingForm
from hotels.models import Hotel


def create_booking(request, hotel_id):

    hotel = get_object_or_404(Hotel, id=hotel_id)

    form = BookingForm(request.POST or None)

    if form.is_valid():

        booking = form.save(commit=False)

        booking.hotel = hotel

        booking.save()

        return redirect('/')

    return render(request, 'bookings/create.html', {
        'form': form,
        'hotel': hotel,
    })
