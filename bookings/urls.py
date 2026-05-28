from django.urls import path
from .views import create_booking

urlpatterns = [

    path('create/<int:hotel_id>/', create_booking, name='create_booking'),

]
