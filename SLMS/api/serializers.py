from rest_framework import serializers
from .models import StreetLight


class StreetLightSerializer(serializers.ModelSerializer):
    class Meta:
        model= StreetLight
        fields=('light_status','comment')

        def create(self, validated_data):
            return StreetLight.objects.create(**validated_data)
