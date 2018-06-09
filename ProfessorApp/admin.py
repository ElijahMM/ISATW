# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from ProfessorApp.models import Professor, Facultate


admin.site.register(Facultate)
admin.site.register(Professor)
