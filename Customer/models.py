from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)  # Set default to None
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    passport_no = models.CharField(max_length=100, null=True)
    pnr_no = models.CharField(max_length=100, null=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    travel_date = models.DateField()
    address = models.TextField(blank=True, null=True)

    BOOKING_TYPES = (
        ('Flight', 'Flight'),
        ('Hotel', 'Hotel'),
        ('Tour', 'Tour'),
    )
    booking_type = models.CharField(max_length=10, choices=BOOKING_TYPES, default='Flight')

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
