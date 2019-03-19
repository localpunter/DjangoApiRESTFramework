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
        customer = self.get_object()
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)



    """
    This will explicitly create a customer, attach the profession & datasheet
    """
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


    def update(self, request, *args, **kwargs):
        customer = self.get_object()
        data = request.data
        customer.name = data['name']
        customer.address = data['address']
        customer.data_sheet_id = data['data_sheet']

        profession = Profession.objects.get(id = data['profession'])

        for p in customer.professions.all():
            customer.professions.remove(p)

        customer.professions.add(profession)
        customer.save()

        serializer = CustomerSerializer(customer)
        return Response(serializer.data)


    def partial_update(self, request, *args, **kwargs):
        customer = self.get_object()
        customer.name = request.data.get('name', customer.name)
        customer.address = request.data.get('address', customer.address)
        customer.data_sheet_id = request.data.get('data_sheet', customer.data_sheet_id)

        customer.save()

        serializer = CustomerSerializer(customer)
        return Response(serializer.data)


    def destroy(self, request, *args, **kwargs):
        customer = self.get_object()
        customer.delete()

        return Response("Object removed!")

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

