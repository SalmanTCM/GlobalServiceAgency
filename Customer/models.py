from django.db import models
from django.contrib.auth.models import User



class Customer(models.Model):
    # user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    passport_no = models.CharField(max_length=100, null=True)
    email = models.EmailField(unique=True, null=True )
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    BOOKING_TYPES = (
        ('Flight', 'Flight'),
        ('Hotel', 'Hotel'),
        ('Tour', 'Tour'),
    )
    booking_type = models.CharField(max_length=10, choices=BOOKING_TYPES, default='Flight', null=True)
    file = models.FileField(upload_to='uploads/', null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


# class salesLog(models.Model):
#     id = models.AutoField(primary_key=True, default=1)
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     agent_name = models.CharField(max_length=100,)
#     ticket_no = models.CharField(max_length=100, null=True)
#     pnr_no = models.CharField(max_length=100, null=True)
#     route = models.CharField(max_length=100, null=True)
#     travel_date = models.DateField()
#     base_fare = models.CharField(max_length=10, null=True)
#     tax = models.CharField(max_length=10, null=True)
#     discount = models.CharField(max_length=10, null=True)
#     ISSUE_TYPES = (
#         ('no_issue', 'no issue'),
#         ('refund', 'refund'),
#         ('reissue', 'reissue'),
#     )
#     issue_types = models.CharField(max_length=10, choices=ISSUE_TYPES, default='no_issue')
#     penalty = models.CharField(max_length=10, blank=True, null=True)
#     refund_price = models.CharField(max_length=10, blank=True, null=True)
#     service_charge = models.CharField(max_length=10, blank=True, null=True)
#
#     # def save(self, *args, **kwargs):
#     #     # Continue with the save
#     #     super(salesLog, self).save(*args, **kwargs)
#     #
#     #     # Update the corresponding AgentLog instance
#     #     update_agent_log(sender=None, instance=self)
#
#
#     def save(self, *args, **kwargs):
#         if self.issue_types == 'refund':
#             self.penalty = ''
#         elif self.issue_types == 'reissue':
#             # Set penalty, refund_price, and service_charge to empty if issue type is reissue
#             self.penalty = ''
#             self.refund_price = ''
#             self.service_charge = ''
#
#         super(salesLog, self).save(*args, **kwargs)
#
#     payment_method = models.CharField(
#         max_length=10,
#         choices=[('bank', 'Bank'), ('mfs', 'Mobile Financial Service'), ('cash', 'Cash')],
#         default='bank'
#     )
#     remarks = models.CharField(max_length=100, blank=True, null=True)
#     date_of_issue = models.DateField()
#
#
#     def customer_price(self):
#         if self.base_fare and self.tax:
#             return int(self.base_fare) + int(self.tax) - int(self.discount)
#         return None
#
#     def __str__(self):
#         return str(self.agent_name)


class salesLog(models.Model):
    # Remove the manually provided default value for id
    id = models.AutoField(primary_key=True)

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    agent_name = models.CharField(max_length=100 , null=True)
    ticket_no = models.CharField(max_length=100, null=True)
    pnr_no = models.CharField(max_length=100, null=True)
    route = models.CharField(max_length=100, null=True)
    travel_date = models.DateField()
    base_fare = models.CharField(max_length=10, null=True)
    tax = models.CharField(max_length=10, null=True)
    discount = models.CharField(max_length=10, null=True)
    ISSUE_TYPES = (
        ('no_issue', 'no issue'),
        ('refund', 'refund'),
        ('reissue', 'reissue'),
    )
    issue_types = models.CharField(max_length=10, choices=ISSUE_TYPES,)
    penalty = models.CharField(max_length=10, blank=True, null=True)
    refund_price = models.CharField(max_length=10, blank=True, null=True)
    service_charge = models.CharField(max_length=10, blank=True, null=True)
    PAYMENT_STATUS_CHOICES = (
        ('paid', 'Paid'),
        ('due', 'Due'),
    )
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES, default='due', null=True)

    paid = models.CharField(max_length=10, null=True)
    due = models.CharField(max_length=10, null=True)


    payment_method = models.CharField(
        max_length=10,
        choices=[('bank', 'Bank'), ('mfs', 'Mobile Financial Service'), ('cash', 'Cash')],
        default='bank'
    )


    remarks = models.CharField(max_length=100, blank=True, null=True)
    date_of_issue = models.DateField()
    created_on = models.DateTimeField(auto_now_add=True, null=True)

    def customer_price(self):
        if self.base_fare and self.tax:
            return int(self.base_fare) + int(self.tax) - int(self.discount)
        return None


    def __str__(self):
        return str(self.agent_name)










