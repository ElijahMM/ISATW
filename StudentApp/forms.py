from django import forms
from django.views.generic import UpdateView

from StudentApp.models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        exclude = ['create_at', 'update_at']

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class StudentFormUpdate(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        exclude = ['create_at', 'update_at', 'cnp', 'nr_matricol']

    def __init__(self, *args, **kwargs):
        super(StudentFormUpdate, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
