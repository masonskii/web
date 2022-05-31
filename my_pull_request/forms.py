from django import forms


class FormsOrgPullRequest(forms.Form):
    person_email = forms.EmailField()
    person_telephone = forms.CharField(max_length=99)
    name_org = forms.CharField(max_length=99)
    logo_org = forms.ImageField()
    type_org = forms.CharField(max_length=99)
    address = forms.CharField(max_length=199)
    description = forms.CharField(widget=forms.Textarea)


class FormsMakesPullRequest(forms.Form):
    role = (
        ('news_makes', 'News Makes'),
        ('task_makes', 'Task Makes')
    )
    name = forms.CharField(max_length=99)
    Role = forms.ChoiceField(choices=role)
    description = forms.CharField(widget=forms.Textarea)
