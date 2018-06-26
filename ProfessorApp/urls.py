from django.conf.urls import url

from ProfessorApp.views import (
    RegisterProfessor,
    ViewProfessors,
    LucreareView,
    ViewLucrari,
    FileUpload,
    ProfesorUpdate,
    DeleteProfesor
)

urlpatterns = [
    url(r'^registerProfessor', RegisterProfessor.as_view(), name='register_professor'),
    url(r'^professor/edit/(?P<pk>[0-9]+)', ProfesorUpdate.as_view(), name='edit_professor'),
    url(r'^professor/delete/(?P<pk>[0-9]+)', DeleteProfesor.as_view(), name='delete_professor'),
    url(r'^viewProfessors', ViewProfessors.as_view(), name='view_professors'),
    url(r'^registerLucrare', LucreareView.as_view(), name='register_lucrare'),
    url(r'^viewLucrare', ViewLucrari.as_view(), name='view_lucrare'),
    url(r'^fileUpload', FileUpload.as_view(), name='file_upload')
]
