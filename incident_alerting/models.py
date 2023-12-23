import enum

from django.db import models


class IncidentStatus(enum.Enum):
	Pending = enum.auto()
	In_Progress = enum.auto()
	Resolved = enum.auto()


class IncidentType(enum.Enum):
	System_Outage = enum.auto()
	Performance_Issue = enum.auto()
	Data_Inconsistency = enum.auto()
	Network_Issue = enum.auto()
	Application_Crash = enum.auto()
	Security_Breach = enum.auto()


class Incident(models.Model):
	incident_id = models.UUIDField(primary_key=True)
	type = models.CharField(max_length=128, choices=[(x.name, x.name) for x in IncidentType])
	severity = models.IntegerField(choices=[(1,1),(2,2),(3,3),(4,4),(5,5)])
	timestamp = models.DateTimeField(auto_now=True)
	description = models.TextField()
	status = models.CharField(max_length=128, choices=[(x.name, x.name) for x in IncidentStatus],
	                          default=IncidentStatus.Pending.name)
	assigned_to = models.CharField(max_length=128, null=True, blank=True, default=None)


class Handler(models.Model):
	name = models.CharField(max_length=64, primary_key=True)
	assigned_incident = models.OneToOneField(Incident,
	                                         on_delete=models.SET_NULL,
	                                         null=True, blank=True, default=None)
