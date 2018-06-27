from django.conf.urls import url
from django.contrib.auth import views as auth_views

from UserApp.views import (
    HomePageView,
    change_password
)

urlpatterns = [
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name="login"),
    url(r'^logout/$', auth_views.logout, {'next_page': 'user_app:home'}, name='logout'),
    url(r'^user/change_password/$', change_password, name='change_password'),
    url(r'^$', HomePageView.as_view(), name="home")
]
