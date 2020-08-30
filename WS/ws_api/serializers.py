from rest_framework import serializers
from .models import WeatherStation


class WeatherStationSerializer(serializers.ModelSerializer):
    class Meta:
        model= WeatherStation
        fields=('device_id','sensor_name','measurement_value')

        def create(self, validated_data):
            return WeatherStation.objects.create(**validated_data)
