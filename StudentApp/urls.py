from django.conf.urls import url

from StudentApp.views import (
    RegisterStudent,
    ViewStudents
)

urlpatterns = [
    url(r'^registerStudent', RegisterStudent.as_view(), name='register_student'),
    url(r'^viewStudents', ViewStudents.as_view(), name='view_students')
]
