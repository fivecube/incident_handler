from django.db.models.signals import post_save
from django.dispatch import receiver

from incident_alerting.incident_handling import handle_incident
from incident_alerting.models import Incident


@receiver(post_save, sender=Incident)
def after_incident_save(sender, **kwargs):
	instance = kwargs.get('instance')
	handle_incident(instance)
