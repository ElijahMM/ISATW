# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import FormView, TemplateView, ListView

from StudentApp.forms import StudentForm
from StudentApp.models import Student


class RegisterStudent(FormView):
    template_name = "register_student.html"
    form_class = StudentForm

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Successfully enrolled.')
        return redirect('user_app:home')


class ViewStudents(ListView):
    template_name = "view_students.html"
    model = Student

    def get_queryset(self):
        query = Student.objects.all()
        return query
