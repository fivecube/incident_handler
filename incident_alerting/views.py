import datetime

from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.generics import GenericAPIView, CreateAPIView, ListAPIView, UpdateAPIView
from incident_alerting.models import Incident, IncidentStatus, Handler
from incident_alerting.serializers import IncidentSerializer
from rest_framework.response import Response

class IncidentView(CreateAPIView,
                   ListAPIView,
                   UpdateAPIView,
				   GenericAPIView):
	serializer_class = IncidentSerializer
	queryset = Incident.objects.all()

	def put(self, request, *args, **kwargs):
		data = request.data
		incident = Incident.objects.filter(incident_id=kwargs.get('instance_id')).first()
		incident.severity = data.get('severity')
		incident.timestamp = datetime.datetime.now()
		incident.status = data.get('status')
		update_fields = ['severity', 'timestamp', 'status']
		if incident.status == IncidentStatus.Resolved.name:
			Handler.objects.filter(assigned_incident=incident).update(assigned_incident=None)
			incident.assigned_to = None
			update_fields.append('assigned_to')
		incident.save(update_fields=update_fields)
		return Response(data , status=status.HTTP_200_OK)
