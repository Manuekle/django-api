from django.apps import AppConfig
# NO se toca

class BaseConfig(AppConfig):
    name = 'base'

    def ready(self):
        import base.signals