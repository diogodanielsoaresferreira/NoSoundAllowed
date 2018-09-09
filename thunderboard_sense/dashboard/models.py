# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Sensor(models.Model):
	name = models.CharField(max_length=100, unique=True, blank=False)

	def __str__(self):
		return str(self.name)


class ValuesReceived(models.Model):
	value = models.FloatField()
	timestamp = models.DateTimeField(auto_now_add=True)
	sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)

	TEMPERATURE = 'TE'
	NOISE = 'NO'
	LED = 'LE'

	VALUE_CHOICES = (
		(NOISE,'Noise'),
		(TEMPERATURE,'Temperature'),
		(LED,'Led'),
	)

	value_type = models.CharField(max_length=2, choices=VALUE_CHOICES)

	def __str__(self):
		return str(self.timestamp) + " - " + str(self.sensor) + " - " + str(self.value_type)

	class Meta:
		verbose_name = "Values Received"
		verbose_name_plural = "Values Received"

