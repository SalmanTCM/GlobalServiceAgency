from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    passport_no = models.CharField(max_length=100, null=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    BOOKING_TYPES = (
        ('Flight', 'Flight'),
        ('Hotel', 'Hotel'),
        ('Tour', 'Tour'),
    )
    booking_type = models.CharField(max_length=10, choices=BOOKING_TYPES, default='Flight')
    file = models.FileField(upload_to='uploads/', null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class salesLog(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    agent_name = models.CharField(max_length=100, primary_key=True)  # Removed null=True
    ticket_no = models.CharField(max_length=100, null=True)
    pnr_no = models.CharField(max_length=100, null=True)
    route = models.CharField(max_length=100, null=True)
    travel_date = models.DateField()
    grand_fare = models.CharField(max_length=10, null=True)
    net_fare = models.CharField(max_length=10, null=True)

    # You can't directly calculate 'profit' as a field like this, use methods or properties for this purpose
    payment_method = models.CharField(
        max_length=10,
        choices=[('bank', 'Bank'), ('mfs', 'Mobile Financial Service'), ('cash', 'Cash')],
        default='bank'
    )
    remarks = models.CharField(max_length=100, blank=True, null=True)
    date_of_issue = models.DateField()

    # Add more fields as needed

    def calculate_profit(self):
        if self.grand_fare and self.net_fare:
            return int(self.grand_fare) - int(self.net_fare)
        return None

    def __str__(self):
        return str(self.agent_name)
