from django.conf.urls import url, include


from StudentApp.views import (
    RegisterStudent
)

urlpatterns = [

    url(r'^registerStudent', RegisterStudent.as_view(), name='register_student')
]
