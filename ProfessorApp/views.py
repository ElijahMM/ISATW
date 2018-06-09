# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import redirect
from django.views.generic import TemplateView, FormView, ListView
from django.contrib import messages
from ProfessorApp.forms import ProfessorForm
from ProfessorApp.models import Professor


class RegisterProfessor(FormView):
    template_name = "register_professor.html"
    form_class = ProfessorForm

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Successfully enrolled.')
        return redirect('register_professor:home')


class ViewProfessors(ListView):
    template_name = "view_professors.html"
    model = Professor

    def get_queryset(self):
        query = Professor.objects.all()
        return query
