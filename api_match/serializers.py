from rest_framework import serializers
from .models import VehicleMatch
 
#Serializers help with translating between JSON, XML, and native Python objects 
class VehicleMatchSerializer(serializers.ModelSerializer):

    class Meta:
        model = VehicleMatch 
        fields = ['pk', 'model_name','make', 'trim']
