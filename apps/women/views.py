from rest_framework import generics
from django.shortcuts import render

from .models import Women
from .serializers import WomenSerializers

# Create your views here.
class WonemAPIViews(generics.ListAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenSerializers
    