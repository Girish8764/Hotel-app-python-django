from django.urls import path
from .views import hotel_detail

urlpatterns = [
    path('<int:id>/', hotel_detail, name='hotel_detail'),
]
