# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import FormView, ListView, UpdateView, DeleteView
from StudentApp.forms import StudentForm, StudentFormUpdate
from StudentApp.models import Facultate
from StudentApp.models import Specializare
from StudentApp.models import Student


# Create your views here.


class RegisterStudent(LoginRequiredMixin, FormView):
    template_name = "register_student.html"
    form_class = StudentForm

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Student inregistrat cu succes.')
        return redirect('student_app:register_student')


class StudentUpdate(LoginRequiredMixin, UpdateView):
    model = Student
    form_class = StudentFormUpdate
    template_name = "edit_student.html"

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Student modificat cu succes.')
        return redirect('student_app:view_students')


class DeleteStudent(LoginRequiredMixin, DeleteView):
    model = Student
    template_name = "student_confirm_delete.html"
    success_url = reverse_lazy('student_app:view_students')


class ViewStudents(LoginRequiredMixin, ListView):
    login_url = 'user_app:home'
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
