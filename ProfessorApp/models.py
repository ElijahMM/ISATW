# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.db import models

from StudentApp.models import Student, Facultate

GENDER_CHOSE = (
    ("M", "Masculin"),
    ("F", "Feminin")
)

LUCRARE_CHOSE = (
    ("L", "Licenta"),
    ("D", "Disertatie")
)


class Professor(models.Model):
    cnp = models.IntegerField(primary_key=True, unique=True, editable=True)
    first_name = models.CharField(max_length=254, blank=True)
    last_name = models.CharField(max_length=254, blank=True)
    phone = models.CharField(max_length=254, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOSE, blank=True)
    email = models.EmailField(unique=True, blank=True)
    create_at = models.DateTimeField(_('create_at'), default=timezone.now)
    update_at = models.DateTimeField(_('update_at'), default=timezone.now)
    faculty = models.ForeignKey(Facultate, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.email

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def get_short_name(self):
        return self.first_name


class Lucrare(models.Model):
    titluLucrare = models.CharField(max_length=254, blank=True)
    tipLucrare = models.CharField(max_length=1, choices=LUCRARE_CHOSE, blank=True)
    create_at = models.DateTimeField(_('create_at'), default=timezone.now)
    update_at = models.DateTimeField(_('update_at'), default=timezone.now)
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    profesor = models.ForeignKey(Professor, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return self.titluLucrare

    def get_full_name(self):
        return self.titluLucrare

    def get_short_name(self):
        return self.titluLucrare


class Document(models.Model):
    descriere = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    create_at = models.DateTimeField(_('create_at'), default=timezone.now)
    update_at = models.DateTimeField(_('update_at'), default=timezone.now)