# customers/urls.py
from django.urls import path
from .views import CustomerList, CustomerDetail
# from .views import ExportExcelView

urlpatterns = [
    path('customers/', CustomerList.as_view(), name='customer-list'),
    path('customers/<int:pk>/', CustomerDetail.as_view(), name='customer-detail'),
    # path('export-excel/', ExportExcelView.as_view(), name='export_excel'),
]
