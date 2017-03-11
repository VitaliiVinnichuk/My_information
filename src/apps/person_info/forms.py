from apps.person_info.models import Person
from apps.person_info.widgets import DatePickerWidget
from django import forms


class PersonForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PersonForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != 'date_of_birth':
                field.widget.attrs['class'] = 'form-control'

    class Meta:
        model = Person
        fields = '__all__'
        widgets = {
            'date_of_birth': DatePickerWidget()
        }
