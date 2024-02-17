from django.contrib import admin

from .models import AgentList, AgentLog


class AgentListAdmin(admin.ModelAdmin):
    list_display = ("agent_name", "email", "phone_number", "payment_method", "remarks")
    search_fields = ("email", "phone_number")

admin.site.register(AgentList,AgentListAdmin)

class AgentLogAdmin(admin.ModelAdmin):
    list_display = ("agent_name", "ticket_no", "travel_date", "base_fare", "paid", "due")
    search_fields = ("agent_name", "ticket_no")
    list_filter = ("travel_date", 'due')


admin.site.register(AgentLog, AgentLogAdmin)
