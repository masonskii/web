from django import forms


class TranslateForm(forms.Form):
    lang_list = (
        ('eng', u'eng'),
        ('rus', u'rus')
    )
    translate = forms.ChoiceField(choices=lang_list, label=None)
