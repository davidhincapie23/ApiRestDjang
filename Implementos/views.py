from django.shortcuts import render
from rest_framework import viewsets
from .models import Balones
from .serealizers import Balonesserializers

# Create your views here.

class BalonesViewSet(viewsets.ModelViewSet):
    serializer_class = Balonesserializers
    queryset = Balones.objects.all()

