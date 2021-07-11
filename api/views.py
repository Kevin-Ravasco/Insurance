from django.shortcuts import render
from rest_framework.generics import ListAPIView

from api.models import Service
from api.serializers import ServicesSerializer


class ServicesList(ListAPIView):
    serializer_class = ServicesSerializer
    queryset = Service.objects.all()
