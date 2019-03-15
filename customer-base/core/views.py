from django.shortcuts import render
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

