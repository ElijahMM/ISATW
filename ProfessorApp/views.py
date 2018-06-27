# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.sites.shortcuts import get_current_site
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import FormView, ListView, UpdateView, DeleteView, DetailView

from ProfessorApp.forms import ProfessorForm, LucrareForm, ProfesorFormUpdate, DocumentForm, StatusForm
from ProfessorApp.models import Professor, Lucrare, Document, LucrareStatus
from StudentApp.models import Facultate, Student
from UserApp.utils import register_new_teacher


class RegisterProfessor(FormView):
    template_name = "register_professor.html"
    form_class = ProfessorForm

    def form_valid(self, form):
        current_site = get_current_site(self.request)
        domain = current_site.domain
        register_new_teacher(form, domain)
        form.save()
        messages.success(self.request, 'Profesor inregistrat cu succes.')
        return redirect('professor_app:register_professor')


class ProfesorUpdate(LoginRequiredMixin, UpdateView):
    model = Professor
    form_class = ProfesorFormUpdate
    template_name = "edit_profesor.html"

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Student modificat cu succes.')
        return redirect('professor_app:view_professors')


class DeleteProfesor(LoginRequiredMixin, DeleteView):
    model = Professor
    template_name = "profesor_confirm_delete.html"
    success_url = reverse_lazy('professor_app:view_professors')


class ViewProfessors(LoginRequiredMixin, ListView):
    template_name = "view_professors.html"
    model = Professor

    def get_queryset(self):
        search_query = self.request.GET.get('search_box', None)
        facult_filter = self.request.GET.get('nfacts', None)
        query = Professor.objects.all()
        facs = Facultate.objects.all()
        if facult_filter:
            query = query.filter(Q(faculty_id=facult_filter)).distinct()
        if search_query:
            query = query.filter(Q(first_name__icontains=search_query) | Q(last_name__icontains=search_query) | Q(
                cnp__icontains=search_query)).distinct()
        return {'professors': query, 'facs': facs}


class ViewLucrari(LoginRequiredMixin, ListView):
    template_name = "view_lucrari.html"
    model = Lucrare

    def get_queryset(self):
        query = Lucrare.objects.all()
        facs = Facultate.objects.all()
        obj = {'lucarari': query, 'facs': facs}
        return obj


class LucreareView(LoginRequiredMixin, FormView):
    template_name = 'register_lucrare.html'
    form_class = LucrareForm

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Lucrare inregistrata cu succes.')
        return redirect('professor_app:register_lucrare')


class UpdateStatusView(LoginRequiredMixin, FormView, ListView):
    template_name = 'register_lucrare_status.html'
    form_class = StatusForm

    def form_valid(self, form):
        if self.request.method == 'POST':
            form = StatusForm(self.request.POST)
            if form.is_valid():
                status = form.save(commit=False)
                status.student = Student.objects.get(nr_matricol=self.kwargs['student_id'])
                status.save()

                return redirect(self.request.path_info)

    def get_queryset(self):
        query = LucrareStatus.objects.filter(student_id=self.kwargs['student_id'])
        obj = {'status': query}
        return obj


class StatusView(LoginRequiredMixin, DetailView):
    template_name = 'view_lucrare_status.html'
    model = LucrareStatus

    def get_object(self, queryset=None):
        status = super(StatusView, self).get_object(queryset=queryset)
        return status


class FileUpload(LoginRequiredMixin, FormView, ListView, View):
    template_name = "file_upload.html"
    form_class = DocumentForm
    model = Document

    def form_valid(self, form):
        if self.request.method == 'POST':
            form = DocumentForm(self.request.POST, self.request.FILES)
            if form.is_valid():
                document = form.save(commit=False)
                document.student = Student.objects.get(nr_matricol=self.kwargs['student_id'])
                document.save()

                return redirect(self.request.path_info)

    def get_queryset(self):
        query = Document.objects.filter(student_id=self.kwargs['student_id'])
        obj = {'documents': query}
        return obj


def pdf_view(request, *args, **kwargs):
    document = Document.objects.get(id=kwargs['document_id'])

    with open(document.document.url, 'r') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'inline;filename=some_file.pdf'
        return response


def delete_status(request, pk):
    status = get_object_or_404(LucrareStatus, id=pk)
    if status:
        status.delete()
    return redirect('professor_app:status_update', student_id=status.student.pk)
