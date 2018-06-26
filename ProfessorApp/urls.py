from django.conf.urls import url

from ProfessorApp.views import (
    RegisterProfessor,
    ViewProfessors,
    LucreareView,
    ViewLucrari,
    FileUpload,
    ProfesorUpdate,
    DeleteProfesor,
    pdf_view,
    UpdateStatusView,
    StatusView,
    DeleteStatus
)

urlpatterns = [
    url(r'^registerProfessor', RegisterProfessor.as_view(), name='register_professor'),
    url(r'^professor/edit/(?P<pk>[0-9]+)', ProfesorUpdate.as_view(), name='edit_professor'),
    url(r'^professor/delete/(?P<pk>[0-9]+)', DeleteProfesor.as_view(), name='delete_professor'),
    url(r'^viewProfessors', ViewProfessors.as_view(), name='view_professors'),
    url(r'^registerLucrare', LucreareView.as_view(), name='register_lucrare'),
    url(r'^viewLucrare', ViewLucrari.as_view(), name='view_lucrare'),
    url(r'^fileUpload/(?P<student_id>\d+)/$', FileUpload.as_view(), name='file_upload'),
    url(r'^student/lucrare/view_pdf/(?P<document_id>\d+)/$', pdf_view, name="pdf_view"),
    url(r'^student/lucrare/update_status/(?P<student_id>\d+)/$', UpdateStatusView.as_view(), name="status_update"),
    url(r'^student/lucrare/status/view/(?P<pk>\d+)/$', StatusView.as_view(), name="view_status"),
    url(r'^student/lucrare/status/delete/(?P<pk>[0-9]+)', DeleteStatus.as_view(), name="delete_status")
]
