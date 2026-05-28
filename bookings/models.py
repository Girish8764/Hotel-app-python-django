from django.db import models
from hotels.models import Hotel


class Booking(models.Model):

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]

    hotel = models.ForeignKey(
        Hotel,
        on_delete=models.CASCADE
    )

    full_name = models.CharField(max_length=255)

    email = models.EmailField()

    phone = models.CharField(max_length=20)

    check_in = models.DateField()

    check_out = models.DateField()

    guests = models.IntegerField(default=1)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
