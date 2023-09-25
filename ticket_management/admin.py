# ticket_management/admin.py

from django.contrib import admin
from .models import Ticket, Agent

admin.site.register(Ticket)
admin.site.register(Agent)
