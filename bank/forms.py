from django import forms


class TransferForms(forms.Form):
    name = forms.CharField()
    number = forms.CharField()
    summary = forms.IntegerField()
    comm = forms.CharField()
