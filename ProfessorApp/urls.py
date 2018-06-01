from django.conf.urls import url


from ProfessorApp.views import (
    RegisterProfessor
)

urlpatterns = [
    url(r'^registerProfessor', RegisterProfessor.as_view(), name='register_professor')
]
