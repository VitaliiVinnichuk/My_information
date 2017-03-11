from django.forms.widgets import DateInput


class DatePickerWidget(DateInput):
    def __init__(self, attrs={}):
        attrs['class'] = 'datepicker form-control'
        super(DatePickerWidget, self).__init__(attrs)
