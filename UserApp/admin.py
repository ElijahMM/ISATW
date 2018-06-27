# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from django.contrib import admin

from StudentApp.models import Facultate, Specializare, Student
from UserApp.models import User


class UsersAdmin(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser', 'is_teacher')


admin.site.register(User, UsersAdmin)

admin.site.register(Facultate)
admin.site.register(Specializare)
admin.site.register(Student)
