from django.db import models
from Customer.models import Customer


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



    def __str__(self):
        return str(self.id)

