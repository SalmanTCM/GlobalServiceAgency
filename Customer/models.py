# customers/models.py
from django.db import models


class Customer(models.Model):
    pax_first_name = models.CharField(max_length=100, null=True)
    pax_last_name = models.CharField(max_length=100, null=True)
    passport_no = models.CharField(max_length=100, null=True)
    pnr_no = models.CharField(max_length=100, null=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    travel_date = models.DateField()
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.pax_first_name} {self.pax_last_name}"