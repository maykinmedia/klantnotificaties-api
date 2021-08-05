from django.contrib import admin

from solo.admin import SingletonModelAdmin

from .models import ServiceConfiguration


@admin.register(ServiceConfiguration)
class ServiceConfigurationAdmin(SingletonModelAdmin):
    pass
