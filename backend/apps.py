from django.apps import AppConfig
from django.db.models.signals import post_save


class BackendConfig(AppConfig):
    name = 'backend'

    def ready(self):
        from backend import signals
        post_save.connect(signals.password_reset_token_created)
        post_save.connect(signals.new_user_registered_signal)
        post_save.connect(signals.new_order_signal)
