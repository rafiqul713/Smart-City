from rest_framework import serializers
from .models import StreetLight


class StreetLightSerializer(serializers.ModelSerializer):
    model = StreetLight
    fields = ("light_status", "comment")
    def create(self, validated_data):
        return StreetLight.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.light_status = validated_data.get('light_status',instance.light_status)
        instance.comment = validated_data.get('comment', instance.comment)
        instance.save()
        return instance
