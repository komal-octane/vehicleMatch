from django.shortcuts import render
from .models import VehicleMatch
from rest_framework import generics
from .serializers import VehicleMatchSerializer


class VehicleCreate(generics.CreateAPIView):
    # API endpoint that allows creation of a new vehicle object
    queryset = VehicleMatch.objects.all(),
    serializer_class = VehicleMatchSerializer

class VehicleList(generics.ListAPIView):
    # API endpoint that allows all vehicles to be viewed.
    queryset = VehicleMatch.objects.all()
    serializer_class = VehicleMatchSerializer

class VehicleDetail(generics.RetrieveAPIView):
    # API endpoint that returns a single vehicle by primary key pk.
    queryset = VehicleMatch.objects.all()
    serializer_class = VehicleMatchSerializer

class VehicleUpdate(generics.RetrieveUpdateAPIView):
    # API endpoint that allows a vehicle record to be updated.
    queryset = VehicleMatch.objects.all()
    serializer_class = VehicleMatchSerializer

class VehicleDelete(generics.RetrieveDestroyAPIView):
    # API endpoint that allows a vehicle record to be deleted.
    queryset = VehicleMatch.objects.all()
    serializer_class = VehicleMatchSerializer    