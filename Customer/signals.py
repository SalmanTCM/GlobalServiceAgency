from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import salesLog
from agent.models import AgentLog
from django.db.models import Sum


# @receiver(post_save, sender=salesLog)
# def update_agent_log(sender, instance, created, **kwargs):
#     # Your logic to update AgentLog based on salesLog changes goes here
#     # For example, you can update the AgentLog instance with the corresponding data
#     if created:
#         agent_name = instance.agent_name
#         ticket_no = instance.ticket_no
#         travel_date = instance.travel_date
#
#         # Query AgentLog using the above criteria and update it accordingly
#         agent_log, created = AgentLog.objects.get_or_create(
#             agent_name=agent_name,
#             ticket_no=ticket_no,
#             travel_date=travel_date
#         )
#         agent_log.save()
@receiver(post_save, sender=salesLog)
def update_agent_log(sender, instance, **kwargs):
    agent_name = instance.agent_name
    ticket_no = instance.ticket_no
    travel_date = instance.travel_date

    # Calculate the total base_fare and total tax from salesLog instances
    total_sales = salesLog.objects.filter(
        agent_name=agent_name, ticket_no=ticket_no, travel_date=travel_date
    )

    total_base_fare = total_sales.aggregate(total_base_fare=Sum('base_fare'))['total_base_fare']
    total_tax = total_sales.aggregate(total_tax=Sum('tax'))['total_tax']

    # Update or create the corresponding AgentLog instance
    agent_log, created = AgentLog.objects.get_or_create(
        agent_name=agent_name, ticket_no=ticket_no, travel_date=travel_date
    )

    # Calculate the total amount (base_fare + tax) and update AgentLog
    total_amount = total_base_fare + total_tax if total_base_fare is not None and total_tax is not None else 0.00
    agent_log.base_fare = total_amount
    agent_log.save()