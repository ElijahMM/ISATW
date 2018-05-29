# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import  FormView

from StudentApp.forms import StudentForm


class RegisterStudent(FormView):
    template_name = "register_student.html"
    form_class = StudentForm

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Successfully enrolled.')
        return redirect('register_profesor:home1')