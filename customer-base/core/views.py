from django.shortcuts import render
from rest_framework.response import Response
from django.http.response import HttpResponseForbidden
from .models import (
    Customer,
    Profession,
    DataSheet,
    Document
    )
from .serializers import (
    CustomerSerializer,
    ProfessionSerializer,
    DataSheetSerializer,
    DocumentSerializer
    )
from rest_framework import viewsets

# ViewSets define the view behavior.
class CustomerViewSet(viewsets.ModelViewSet):
    serializer_class = CustomerSerializer

    def get_queryset(self):
        active_customers = Customer.objects.filter(active = True)
        return active_customers

    def list(self, request, *args, **kwargs):
        customers = Customer.objects.filter(id=3)
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)


    def retrieve(self, request, *args, **kwargs):
        return HttpResponseForbidden("Not allowed")
        # obj = self.get_object()
        # serializer = CustomerSerializer(obj)
        # return Response(serializer.data)


    """This will explicitly create a customer, attach the profession & datasheet"""
    def create(self, request, *args, **kwargs):
        data = request.data
        customer = Customer.objects.create(
            name = data['name'], address = data['address'], data_sheet_id = data['data_sheet']
        )
        profession = Profession.objects.get(id = data['profession'])
        customer.professions.add(profession)
        customer.save()

        serializer = CustomerSerializer(customer)
        return Response(serializer.data)


class ProfessionViewSet(viewsets.ModelViewSet):
    serializer_class = ProfessionSerializer

    def get_queryset(self):
        active_professions = Profession.objects.filter(active = True)
        return active_professions


class DataSheetViewSet(viewsets.ModelViewSet):
    serializer_class = DataSheetSerializer

    def get_queryset(self):
        active_datasheets = DataSheet.objects.filter(active = True)
        return active_datasheets


class DocumentViewSet(viewsets.ModelViewSet):
    serializer_class = DocumentSerializer

    def get_queryset(self):
        active_documents = Document.object.filter(active = True)
        return active_documents

