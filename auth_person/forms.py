import datetime

from django import forms



class PersonRegistrationForms(forms.Form):

    login = forms.CharField(
        label='login',
        help_text='enter your login',
        min_length=3,
        max_length=20,
    )
    password = forms.CharField(
        label='password',
        help_text='enter your password',
        min_length=6,
        max_length=32,
    )
    name = forms.CharField(
        label='name',
        help_text='enter your name',
        max_length=30,
    )
    surname = forms.CharField(
        label='surname',
        help_text='enter your surname',
        max_length=30,
    )
    ndName = forms.CharField(
        label='ndName',
        help_text='enter your ndName',
        max_length=30,
        required=False,
    )
    birthday = forms.DateField(
        label='birthday',
        help_text='enter your birthday',
        initial=datetime.date.today()
    )
    logo = forms.ImageField()


class SignIn(forms.Form):
    login = forms.CharField(
        label='login',
        help_text='enter your login',
        min_length=3,
        max_length=20,
    )
    password = forms.CharField(
        label='password',
        help_text='enter your password',
        min_length=6,
        max_length=32,
    )