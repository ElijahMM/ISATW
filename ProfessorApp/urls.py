from django.conf.urls import url

from ProfessorApp.views import (
    RegisterProfessor,
    ViewProfessors,
    LucreareView,
    ViewLucrari,
    FileUpload,
    ProfesorUpdate,
    delete_profesor,
    pdf_view,
    UpdateStatusView,
    StatusView,
    delete_status,
    delete_document,
    delete_lucrare,
)

urlpatterns = [
    url(r'^registerProfessor', RegisterProfessor.as_view(), name='register_professor'),
    url(r'^professor/edit/(?P<pk>[0-9]+)', ProfesorUpdate.as_view(), name='edit_professor'),
    url(r'^professor/delete/(?P<pk>[0-9]+)', delete_profesor, name='delete_professor'),
    url(r'^viewProfessors', ViewProfessors.as_view(), name='view_professors'),
    url(r'^registerLucrare', LucreareView.as_view(), name='register_lucrare'),
    url(r'^viewLucrare', ViewLucrari.as_view(), name='view_lucrare'),
    url(r'^fileUpload/(?P<student_id>\d+)/$', FileUpload.as_view(), name='file_upload'),
    url(r'^student/lucrare/view_pdf/(?P<document_id>\d+)/$', pdf_view, name="pdf_view"),
    url(r'^student/lucrare/update_status/(?P<student_id>\d+)/$', UpdateStatusView.as_view(), name="status_update"),
    url(r'^student/lucrare/status/view/(?P<pk>\d+)/$', StatusView.as_view(), name="view_status"),
    url(r'^student/lucrare/status/delete/(?P<pk>[0-9]+)', delete_status, name="delete_status"),
    url(r'^student/lucrare/document/delete/(?P<pk>[0-9]+)', delete_document, name="delete_document"),
    url(r'^student/lucrare/delete/(?P<pk>[0-9]+)', delete_lucrare, name="delete_lucrare"),
]
