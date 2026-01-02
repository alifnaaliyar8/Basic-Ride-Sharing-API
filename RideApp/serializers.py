from rest_framework import serializers
from RideApp.models import Ride

class RideSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = '__all__'
        read_only_fields = ['rider', 'status', 'created_at', 'updated_at']


class RideStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = ['status']


class RideTrackingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ride
        fields = ['current_location']
