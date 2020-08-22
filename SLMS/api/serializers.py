from rest_framework import serializers
from .models import StreetLight


class StreetLightSerializer(serializers.ModelSerializer):
    class Meta:
        model= StreetLight
        fields=('device_id','light_status')

        def create(self, validated_data):
            return StreetLight.objects.create(**validated_data)
