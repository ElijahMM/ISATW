# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.shortcuts import render, redirect, render_to_response
# Create your views here.
from django.views.generic import FormView, TemplateView, ListView
from StudentApp.forms import StudentForm
from StudentApp.models import Student
from StudentApp.models import Facultate
from StudentApp.models import Specializare


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
        print("ViewStudents")
        query = Student.objects.all()
        facs = Facultate.objects.all()
        specs = Specializare.objects.all()
        obj = {'students': query, 'facs': facs, 'specs': specs}
        return obj


class ViewStudentsQueryFacuty(ListView):
    template_name = "view_students.html"
    model = Student

    def get_queryset(self):
        query = Student.objects.filter(faculty=self.kwargs['facultate_id'])
        facs = Facultate.objects.all()
        specs = Specializare.objects.all()
        obj = {'students': query, 'facs': facs, 'specs': specs}
        return obj


class ViewStudentsQueryScec(ListView):
    template_name = "view_students.html"
    model = Student

    def get_queryset(self):
        a = self.request.GET
        print(a)


        query = Student.objects.filter(specializations=self.kwargs['specialization_id'])
        facs = Facultate.objects.all()
        specs = Specializare.objects.all()
        obj = {'students': query, 'facs': facs, 'specs': specs}
        return obj


class ViewStudentsQueryAll(ListView):
    template_name = "view_students.html"
    model = Student

    def get_queryset(self):
        query = Student.objects.filter(faculty=self.kwargs['facultate_id'],
                                       specialization=self.kwargs['specialization_id'])
        facs = Facultate.objects.all()
        specs = Specializare.objects.all()
        obj = {'students': query, 'facs': facs, 'specs': specs}
        return obj
