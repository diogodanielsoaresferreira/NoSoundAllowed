# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from dashboard.models import Sensor, ValuesReceived
import json


@login_required(login_url="login")
def index(request):

	sensors = Sensor.objects.all()
	sensor_values = {}

	for s in sensors:
		try:
			temp_values = ValuesReceived.objects.filter(sensor=s, value_type=ValuesReceived.TEMPERATURE).order_by('-timestamp')[0].value
		except Exception as e:
			temp_values = []

		try:
			noise_values = ValuesReceived.objects.filter(sensor=s, value_type=ValuesReceived.NOISE).order_by('-timestamp')[0].value
		except Exception as e:
			noise_values = []

		sensor_values[s.name] = {"temperature": temp_values, "noise": noise_values}

	return render(request, 'adminlte/index.html', {'sensors': sensor_values})


@login_required(login_url="login")
def history(request):

	sensor_temperature_values = {}
	sensor_noise_values = {}
	temperature_values = ValuesReceived.objects.filter(value_type=ValuesReceived.TEMPERATURE).values_list("value", "timestamp", "sensor")

	for temperature in temperature_values:
		value = temperature[0]
		timestamp = temperature[1]
		sensor = Sensor.objects.get(id=temperature[2]).name

		if sensor in sensor_temperature_values:
			sensor_temperature_values[sensor] += [([timestamp.year, timestamp.month, timestamp.day, timestamp.hour, timestamp.minute, timestamp.second], value)]

		else:
			sensor_temperature_values[sensor] = [([timestamp.year, timestamp.month, timestamp.day, timestamp.hour, timestamp.minute, timestamp.second], value)]


	noise_values = ValuesReceived.objects.filter(value_type=ValuesReceived.NOISE).values_list("value", "timestamp", "sensor")

	for noise in noise_values:
		value = noise[0]
		timestamp = noise[1]
		sensor = Sensor.objects.get(id=noise[2]).name

		if sensor in sensor_noise_values:
			sensor_noise_values[sensor] += [([timestamp.year, timestamp.month, timestamp.day, timestamp.hour, timestamp.minute, timestamp.second], value)]

		else:
			sensor_noise_values[sensor] = [([timestamp.year, timestamp.month, timestamp.day, timestamp.hour, timestamp.minute, timestamp.second], value)]


	return render(request, 'adminlte/history.html', {"temperature": json.dumps(sensor_temperature_values), "noise": json.dumps(sensor_noise_values)})



