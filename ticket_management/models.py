# ticket_management/models.py

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

class salesLog(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    route = models.CharField(max_length=100, null=True)
    ticket_no = models.CharField(max_length=100, null=True)
    total = models.CharField(max_length=100)
    received = models.CharField(max_length=100)
    status = models.CharField(max_length=100)
    remains = models.CharField(max_length=100)
    sale_date = models.DateField()
    # Add more fields as needed


class ticket_management (models.Model):
    status = models.CharField(max_length=100, null=True)