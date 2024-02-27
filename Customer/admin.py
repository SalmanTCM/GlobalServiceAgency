from django.contrib import admin
from .models import Customer, salesLog
from rangefilter.filters import DateRangeFilter
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from import_export.admin import ExportMixin

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'passport_no', 'email', 'phone_number', 'address', 'booking_type', 'file', 'display_image')
    list_filter = ('booking_type', 'passport_no')
    search_fields = ('passport_no', 'email', 'phone_number')
    list_per_page = 10

    def display_image(self, obj):
        if obj.file:
            return mark_safe(f'<img src="{obj.file.url}" width="50" height="50" />')
        return "No Image"

admin.site.register(Customer, CustomerAdmin)


class SalesLogAdmin(ExportMixin, admin.ModelAdmin):
    list_display = (
        'customer', 'agent_name', 'ticket_no', 'pnr_no', 'route', 'travel_date', 'base_fare','tax','customer_price','net_fare', 'commission',
         'discount','net_profit',
        'payment_method', 'remarks', 'date_of_issue',
         'paid', 'due', 'payment_status_colored', 'created_on', 'issue_types_colored',
    )
    list_editable = ('discount',)
    list_filter = (("travel_date", DateRangeFilter),'route', 'agent_name','date_of_issue')
    search_fields = ('customer', 'ticket_no', 'pnr_no', 'route', 'remarks', 'agent_name')
    actions = ['export_admin_action']
    list_per_page = 10

    def payment_status_colored(self, obj):
        # Display payment_status with colored text, background, padding, and border radius
        text_color = 'white'
        background_color = 'green' if obj.payment_status == 'paid' else 'red'
        padding = '8px'
        border_radius = '5px'
        return format_html(
            '<span style="color: {}; background-color: {}; padding: {}; border-radius: {};">{}</span>',
            text_color, background_color, padding, border_radius, obj.get_payment_status_display()
        )

    payment_status_colored.short_description = 'Payment Status'

    def issue_types_colored(self, obj):
        color = 'green' if obj.issue_types == 'no_issue' else 'red'

        # Conditionally show or hide additional fields based on issue_types
        additional_fields = ''
        if obj.issue_types in ['refund', 'reissue']:
            additional_fields = format_html(
                '<br>penalty: {penalty}, refund: {refund}, service: {service}',
                penalty=obj.penalty,
                refund=obj.refund_price,
                service=obj.service_charge
            )

        return format_html(
            '<span style="color: {};">{}</span>{}',
            color, obj.issue_types, additional_fields
        )

    issue_types_colored.short_description = 'Issue Types'

    class Media:
        js = ("admin/js/custom_admin.js",)




admin.site.register(salesLog, SalesLogAdmin)

