# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from ProfessorApp.models import Professor, Lucrare, Document

admin.site.register(Professor)
admin.site.register(Lucrare)
admin.site.register(Document)
