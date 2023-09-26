# ticket_management/admin.py

from django.contrib import admin
from .models import Ticket, Agent

class TicketAdmin(admin.ModelAdmin):
    list_display = ('customer', 'agent', 'from_location', 'to_location', 'departure_date', 'ticket_class', 'quantity', 'note', 'amount', 'received', 'payment', 'paid', 'terminated', 'created_at', 'updated_at')
    list_filter = ('customer', 'from_location')
    search_fields = ('ticket_class', 'agent', 'customer', 'terminated')

admin.site.register(Ticket, TicketAdmin)


class AgentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'payment_method', 'remarks')
    list_filter = ('payment_method',)
    search_fields = ('phone_number', 'email')

admin.site.register(Agent, AgentAdmin)