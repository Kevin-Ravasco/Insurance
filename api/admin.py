from django.contrib import admin

from api.models import Service


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']
    search_fields = ['name', 'price']


admin.site.register(Service, ServiceAdmin)

