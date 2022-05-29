from django.apps import AppConfig


class MfestivalUsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'mfestival_users'

    def ready(self):
        import mfestival_users.signals
