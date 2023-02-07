from rest_framework import serializers
from .models import Transport,Car_type,shipment,Cars

class Transportserializer(serializers.ModelSerializer):
    class Meta:
        model= Transport
        exclude=["created_at","updated_at"]

class Car_typeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Car_type
        exclude=["created_at","updated_at"]

class shipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model=shipment
        exclude=["created_at","updated_at"]

class carSerializer(serializers.ModelSerializer):
    class Meta:
        model=Cars
        exclude=["created_at","updated_at"]