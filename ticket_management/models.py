from django.db import models
from Customer.models import Customer


class Ticket(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    # agent = models.ForeignKey('Agent', on_delete=models.CASCADE)
    from_location = models.CharField(max_length=255)
    to_location = models.CharField(max_length=255)
    departure_date = models.DateField()
    ticket_class = models.CharField(max_length=50)
    quantity = models.IntegerField()
    note = models.TextField(blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    received = models.BooleanField(default=False)
    payment = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    paid = models.BooleanField(default=False)
    terminated = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Ticket #{self.id} - {self.customer.first_name} {self.customer.last_name}"





