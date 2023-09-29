from django.db import models
from decimal import Decimal
from Customer.models import salesLog


class AgentList(models.Model):
    agent_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    payment_method = models.CharField(
        max_length=10,
        choices=[('bank', 'Bank'), ('mfs', 'Mobile Financial Service'), ('cash', 'Cash')],
        default='bank'
    )
    remarks = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.agent_name}"

    def __str__(self):
        return f"Agent #{self.id}"


class AgentLog(models.Model):
        agent_name = models.CharField(max_length=100, null=True)
        ticket_no = models.CharField(max_length=100, null=True)
        travel_date = models.DateField()
        grand_fare = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
        paid = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
        due = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

        def __str__(self):
            return str(self.id)

        def save(self, *args, **kwargs):
            # Calculate the 'grand_fare' field by aggregating sales from SalesLog
            sales = salesLog.objects.filter(agent_name=self.agent_name, ticket_no=self.ticket_no,
                                            travel_date=self.travel_date)
            total_fare = sum([Decimal(sale.grand_fare) for sale in sales])
            self.grand_fare = total_fare

            super().save(*args, **kwargs)