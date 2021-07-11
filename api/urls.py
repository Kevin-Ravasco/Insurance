from django.urls import path

from api.views import ServicesList

urlpatterns = [
    path('', ServicesList.as_view(), name='services'),
]
