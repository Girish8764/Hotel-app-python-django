from django.shortcuts import render, get_object_or_404
from .models import Hotel


def hotel_detail(request, id):

    hotel = get_object_or_404(Hotel, id=id)

    return render(request, 'hotels/detail.html', {
        'hotel': hotel
    })
