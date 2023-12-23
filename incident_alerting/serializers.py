from rest_framework.serializers import ModelSerializer

from incident_alerting.models import Incident


class IncidentSerializer(ModelSerializer):
	class Meta:
		model = Incident
		fields = ['incident_id', 'type', 'severity', 'timestamp', 'description', 'status']
