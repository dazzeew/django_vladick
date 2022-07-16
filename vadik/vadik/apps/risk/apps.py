from django.apps import AppConfig


class RiskConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'risk'
    verbose_name = 'Валюты и транзакции'

    def ready(self):
        from . import signals