# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from dashboard.models import Sensor, ValuesReceived
from django.contrib.auth.models import Group

# Register your models here.
admin.site.register(Sensor)
admin.site.register(ValuesReceived)
admin.site.unregister(Group)