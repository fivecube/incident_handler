from incident_alerting.models import Incident, IncidentStatus, Handler


def assign_incident(handler, incident):
	handler.assigned_incident = incident
	handler.save()
	incident.assigned_to = handler.name
	incident.status = IncidentStatus.In_Progress.name
	incident.save(update_fields=['assigned_to', 'status'])


def immediate_assignment_to_available_handler(incident):
	if incident.status == IncidentStatus.Resolved.name:
		return
	for handler in Handler.objects.filter(assigned_incident=None):
		assign_incident(handler, incident)
		break


def handle_incident(incident):
	for pending_incident in Incident.objects.filter(status=IncidentStatus.Pending.name,
	                                                assigned_to=None).order_by('severity', 'timestamp'):
		immediate_assignment_to_available_handler(pending_incident)