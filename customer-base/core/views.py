from django.shortcuts import render
from .models import Customer
from .serializers import CustomerSerializer
from rest_framework import viewsets

# ViewSets define the view behavior.
class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
