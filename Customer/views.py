# customers/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Customer
from .serializers import CustomerSerializer
from .models import salesLog
from django.http import HttpResponse
from django.views.generic import View
# from .resources import salesLogResource
from import_export.resources import ModelResource



class CustomerList(APIView):
    def get(self, request):
        customers = Customer.objects.all()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CustomerDetail(APIView):
    def get_object(self, pk):
        try:
            return Customer.objects.get(pk=pk)
        except Customer.DoesNotExist:
            raise status.HTTP_404_NOT_FOUND

    def get(self, request, pk):
        customer = self.get_object(pk)
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    def put(self, request, pk):
        customer = self.get_object(pk)
        serializer = CustomerSerializer(customer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        customer = self.get_object(pk)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class ExportExcelView(View):
#     def get(self, request, *args, **kwargs):
#         dataset = salesLogResource().export(salesLog.objects.all())
#         response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
#         response['Content-Disposition'] = 'attachment; filename=sales_logs.xls'
#         return response
