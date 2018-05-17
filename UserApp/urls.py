from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views

from UserApp.views import (
    HomePageView
)

urlpatterns = [
    url(r'^login', auth_views.login, {'template_name': 'login.html'}, name="login"),
    url(r'^$', HomePageView.as_view(), name="home"),
]
