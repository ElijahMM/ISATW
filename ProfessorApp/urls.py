from django.conf.urls import url


from ProfessorApp.views import (
    RegisterProfessor,
    ViewProfessors
)

urlpatterns = [
    url(r'^registerProfessor', RegisterProfessor.as_view(), name='register_professor'),
    url(r'^viewProfessors', ViewProfessors.as_view(), name='view_professors')
]
