from django.apps import AppConfig
from django.db.models.signals import pre_save

class BackendConfig(AppConfig):
    name = 'backend'

    def ready(self):
        """
        импортируем сигналы
        """

