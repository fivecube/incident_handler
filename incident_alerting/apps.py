from django.apps import AppConfig


class IncidentAlertingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'incident_alerting'

    def ready(self):
        import incident_alerting.signals  # noqa
