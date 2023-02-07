from django.apps import AppConfig


class SiloConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'silo'

    def ready(self):
        import silo.signals
