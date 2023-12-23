from django.contrib import admin

# Register your models here.
from incident_alerting.models import Incident, Handler


@admin.register(Incident)
class IncidentAdmin(admin.ModelAdmin):
	fields = [
		'incident_id',
		'type',
		'severity',
		'timestamp',
		'description',
		'status',
		'assigned_to'
	]
	list_display = ['incident_id',
	                'type',
	                'status',
	                'severity',
	                'assigned_to']
	search_fields = [
		'assigned_to',
		'incident_id'
	]
	list_filter = [
		'type',
		'severity',
		'status'
	]


@admin.register(Handler)
class HandlerAdmin(admin.ModelAdmin):
	fields = [
	'name',
	'assigned_incident'
	]
	list_display = ['name',
	                'assigned_incident']
	search_fields = [
		'name',
		'assigned_incident'
	]