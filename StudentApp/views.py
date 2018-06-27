# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import redirect, get_object_or_404
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
        search_query = self.request.GET.get('search_box', None)
        facult_filter = self.request.GET.get('nfacts', None)
        spec_filter = self.request.GET.get('sfacts', None)
        query = Student.objects.all()
        facs = Facultate.objects.all()
        specs = Specializare.objects.all()
        if facult_filter:
            query = query.filter(Q(faculties_id=facult_filter)).distinct()
        if spec_filter:
            query = query.filter(Q(specializations_id=spec_filter)).distinct()
        if search_query:
            query = query.filter(Q(first_name__icontains=search_query) | Q(last_name__icontains=search_query) | Q(
                nr_matricol__icontains=search_query)).distinct()
        return {'students': query, 'facs': facs, 'specs': specs}


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


def delete_student(request, pk):
    student = get_object_or_404(Student, nr_matricol=pk)
    if student:
        student.delete()
    return redirect('student_app:view_students')
