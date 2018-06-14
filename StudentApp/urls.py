from django.conf.urls import url

from StudentApp.views import (
    RegisterStudent,
    ViewStudents,
    ViewStudentsQueryFacuty,
    ViewStudentsQueryScec,
    ViewStudentsQueryAll

)

urlpatterns = [
    url(r'^registerStudent', RegisterStudent.as_view(), name='register_student'),
    url(r'^viewStudents', ViewStudents.as_view(), name='view_students'),
    url(r'^filter/facultate/(?P<facultate_id>\d+)/$', ViewStudentsQueryFacuty.as_view(), name='view_students_f'),
    url(r'^filter/specializare/(?P<specialization_id>\d+)/$', ViewStudentsQueryScec.as_view(), name='view_students_s'),
    url(r'^filter/all/(?P<facultate_id>\d+)/(?P<specialization_id>\d+)/$', ViewStudentsQueryAll.as_view(),
        name='view_students_fs'),
]
