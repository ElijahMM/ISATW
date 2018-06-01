# -*- coding: utf-8 -*-
from __future__ import unicode_literals



# Create your views here.
from django.views.generic import TemplateView


from UserApp.models import User


class HomePageView(TemplateView, User):
    if User.is_superuser:
        template_name = 'home.html'
    else:
        template_name = 'home1.html'


class LoginPageView(TemplateView):
    template_name = 'login.html'
