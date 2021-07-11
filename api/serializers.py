from rest_framework import serializers

from api.models import Service


class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'image', 'name', 'description', 'price']