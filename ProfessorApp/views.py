# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.mixins import LoginRequiredMixin
<<<<<<< HEAD
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, FormView, ListView
from django.contrib import messages
from ProfessorApp.forms import ProfessorForm, LucrareForm, DocumentForm
from ProfessorApp.models import Professor, Lucrare, Document
=======
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, ListView, UpdateView, DeleteView
from django.contrib import messages
from ProfessorApp.forms import ProfessorForm, LucrareForm, ProfesorFormUpdate
from ProfessorApp.models import Professor, Lucrare
>>>>>>> 3578a04bb36aa43b9ac3c244b5435d7302ed27ea
from StudentApp.models import Facultate


class RegisterProfessor(FormView):
    template_name = "register_professor.html"
    form_class = ProfessorForm

    def form_valid(self, form):
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


class ViewProfessors(ListView):
    template_name = "view_professors.html"
    model = Professor

    def get_queryset(self):
        query = Professor.objects.all()
        facs = Facultate.objects.all()
        obj = {'professors': query, 'facs': facs}
        return obj


class ViewLucrari(ListView):
    template_name = "view_lucrari.html"
    model = Lucrare

    def get_queryset(self):
        query = Lucrare.objects.all()
        facs = Facultate.objects.all()
        obj = {'lucarari': query, 'facs': facs}
        return obj


class FileUpload(FormView, ListView):
    template_name = "file_upload.html"
    form_class = DocumentForm
    model = Document

    def form_valid(self, form):
        if self.request.method == 'POST':
            form = DocumentForm(self.request.POST, self.request.FILES)
            if form.is_valid():
                form.save()

        return redirect('professor_app:file_upload')

    def get_queryset(self):
        query = Document.objects.all()
        obj = {'documents': query}
        return obj


class LucreareView(FormView):
    template_name = 'register_lucrare.html'
    form_class = LucrareForm

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Lucrare inregistrata cu succes.')
        return redirect('professor_app:register_lucrare')
