from django import forms

from ProfessorApp.models import Professor, Lucrare, Document
from StudentApp.models import Student, Facultate


class ProfessorForm(forms.ModelForm):
    class Meta:
        model = Professor
        fields = '__all__'
        exclude = ['create_at', 'update_at']

    def __init__(self, *args, **kwargs):
        super(ProfessorForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

        self.fields['faculty'].queryset = Facultate.objects.all()


class LucrareForm(forms.ModelForm):
    class Meta:
        model = Lucrare
        fields = '__all__'
        exclude = ['create_at', 'update_at']

    def __init__(self, *args, **kwargs):
        super(LucrareForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = '__all__'
        exclude = ['create_at', 'update_at']