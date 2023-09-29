from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import salesLog
from agent.models import AgentLog

@receiver(post_save, sender=salesLog)
def update_agent_log(sender, instance, created, **kwargs):
    # Your logic to update AgentLog based on salesLog changes goes here
    # For example, you can update the AgentLog instance with the corresponding data
    if created:
        agent_name = instance.agent_name
        ticket_no = instance.ticket_no
        travel_date = instance.travel_date

        # Query AgentLog using the above criteria and update it accordingly
        agent_log, created = AgentLog.objects.get_or_create(
            agent_name=agent_name,
            ticket_no=ticket_no,
            travel_date=travel_date
        )
        agent_log.save()
