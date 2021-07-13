from django.apps import AppConfig


class UtilsConfig(AppConfig):
    name = "klantnotificaties.utils"

    def ready(self):
        from . import checks  # noqa
