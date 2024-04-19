from django.shortcuts import render

# Create your views here.
from .serializer import TransporteSerializer
from .models import Transporte
from rest_framework import viewsets

class TransporteViewset(viewsets.ModelViewSet):
    queryset = Transporte.objects.all()
    serializer_class= TransporteSerializer