from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(
        required=True, min_length=4, max_length=32, strip=True)
    password = forms.CharField(
        required=True, min_length=8, max_length=32, strip=True, widget=forms.PasswordInput)
    password_repeat = forms.CharField(
        required=True, min_length=8, max_length=32, strip=True, widget=forms.PasswordInput)


class LoginForm(forms.Form):
    username = forms.CharField(
        required=True, min_length=4, max_length=32, strip=True)
    password = forms.CharField(
        required=True, min_length=8, max_length=32, strip=True, widget=forms.PasswordInput)


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


class QualityRatingForm(forms.Form):
    CHOICES = [(i, str(i)) for i in range(1, 11)]
    rating = forms.ChoiceField(
        widget=forms.RadioSelect,
        choices=CHOICES,
        required=True,
    )
