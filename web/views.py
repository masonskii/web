from django.http import HttpResponseRedirect
from django.shortcuts import render

from abstract.AbstractUserModel import Translate
from abstract.parsing_translate import ParsingTranslate
from event.models import Task
from my_pull_request.forms import FormsOrgPullRequest
from my_pull_request.models import OrgPullRequest
from news.models import News
from web.forms import TranslateForm


def index(request):
    if 'request_org' in request.POST:
        OrgPullRequest(
            person_email=request.POST['reg_org_person_email'],
            person_telephone=request.POST['reg_org_person_phone'],
            name_org=request.POST['reg_org_name'],
            address=request.POST['reg_org_address'],
            type_org=request.POST['reg_org_type'],
            logo_org=request.FILES['reg_org_logo'],
            description=request.POST['reg_org_description'],
        ).save()
        return HttpResponseRedirect("/")
    if 'switch-lang' in request.POST:
        if request.POST.get('translate') == 'rus':
            _ = Translate.objects.filter(id=1).update(translate=1)
            print(request.POST.get('translate'))
            lang = ParsingTranslate.open_file(1)
            form_tr = TranslateForm()
            return render(request, 'index.html', {
                'form_tr': form_tr,
                'news': News.objects.filter(is_actual=True),
                'task': Task.objects.all(),
                "NameApp": lang["NameApp"],
                "Bank": lang["Bank"],
                "cNews": lang["cNews"],
                "News": lang["News"],
                "oNews": lang["oNews"],
                "cTask": lang["cTask"],
                "SignIn": lang["SignIn"],
                "SignUp": lang["SignUp"],
                "LK": lang["LK"],
                "Logout": lang["Logout"],
                "Dashboard": lang["Dashboard"],
                "Events": lang["Events"],
                "Market": lang["Market"],
                "Profile": lang["Profile"],
                "Menu": lang["Menu"],
                "cEvent": lang["cEvent"],
                "RequestPullOrg": lang["RequestPullOrg"],

            })
        else:
            _ = Translate.objects.filter(id=1).update(translate=0)
            lang = ParsingTranslate.open_file(0)
            form_tr = TranslateForm()
            return render(request, 'index.html', {
                'form_tr': form_tr,
                'news': News.objects.filter(is_actual=True),
                'old_news': News.objects.filter(is_actual=False),
                'task': Task.objects.all(),
                "NameApp": lang["NameApp"],
                "Bank": lang["Bank"],
                "cNews": lang["cNews"],
                "News": lang["News"],
                "oNews": lang["oNews"],
                "cTask": lang["cTask"],
                "SignIn": lang["SignIn"],
                "SignUp": lang["SignUp"],
                "LK": lang["LK"],
                "Logout": lang["Logout"],
                "Dashboard": lang["Dashboard"],
                "Events": lang["Events"],
                "Market": lang["Market"],
                "Profile": lang["Profile"],
                "Menu": lang["Menu"],
                "cEvent": lang["cEvent"],
                "RequestPullOrg": lang["RequestPullOrg"],

            })
    else:
        t = Translate.objects.get(id=1)
        if t.translate == 0:
            lang = ParsingTranslate.open_file(0)
            form_tr = TranslateForm()
            return render(request, 'index.html', {
                'form_tr': form_tr,
                'news': News.objects.filter(is_actual=True),
                'old_news': News.objects.filter(is_actual=False),
                'task': Task.objects.all(),
                "NameApp": lang["NameApp"],
                "Bank": lang["Bank"],
                "cNews": lang["cNews"],
                "News": lang["News"],
                "oNews": lang["oNews"],
                "cTask": lang["cTask"],
                "SignIn": lang["SignIn"],
                "SignUp": lang["SignUp"],
                "LK": lang["LK"],
                "Logout": lang["Logout"],
                "Dashboard": lang["Dashboard"],
                "Events": lang["Events"],
                "Market": lang["Market"],
                "Profile": lang["Profile"],
                "Menu": lang["Menu"],
                "cEvent": lang["cEvent"],
                "RequestPullOrg": lang["RequestPullOrg"],
            })
        else:
            lang = ParsingTranslate.open_file(1)
            form_tr = TranslateForm()
            return render(request, 'index.html', {
                'form_tr': form_tr,
                'news': News.objects.filter(is_actual=True),
                'old_news': News.objects.filter(is_actual=False),
                'task': Task.objects.all(),
                "NameApp": lang["NameApp"],
                "Bank": lang["Bank"],
                "CreateNews": lang["cNews"],
                "News": lang["News"],
                "oNews": lang["oNews"],
                "CreateTask": lang["cTask"],
                "SignIn": lang["SignIn"],
                "SignUp": lang["SignUp"],
                "LK": lang["LK"],
                "Logout": lang["Logout"],
                "Dashboard": lang["Dashboard"],
                "Events": lang["Events"],
                "Market": lang["Market"],
                "Profile": lang["Profile"],
                "Menu": lang["Menu"],
                "CreateEvents": lang["cEvent"],
                "RequestPullOrg": lang["RequestPullOrg"],
            })
