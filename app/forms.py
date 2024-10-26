from django import forms


class AlarmForm(forms.Form):
    time = forms.TimeField(required=True)
    day1 = forms.CheckboxInput()
    day2 = forms.CheckboxInput()
    day3 = forms.CheckboxInput()
    day4 = forms.CheckboxInput()
    day5 = forms.CheckboxInput()
    day6 = forms.CheckboxInput()
    day7 = forms.CheckboxInput()
    n_repeats = forms.DecimalField(required=True, min_value=0, max_value=5)
