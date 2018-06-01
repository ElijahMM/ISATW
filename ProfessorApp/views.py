# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import redirect
from django.views.generic import TemplateView, FormView
from django.contrib import messages
from ProfessorApp.forms import ProfessorForm


class RegisterProfessor(FormView):
    template_name = "register_professor.html"
    form_class = ProfessorForm

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Successfully enrolled.')
        return redirect('register_professor:home')
