import datetime
from datetime import timezone

from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.shortcuts import render

from abstract.AbstractUserModel import Translate
from abstract.parsing_translate import ParsingTranslate
from auth_person.models import Person
from event.models import Task
from my_pull_request.forms import FormsOrgPullRequest
from my_pull_request.models import OrgPullRequest
from news.models import News
from web.forms import TranslateForm


def index(request):
    if 'request_org' in request.POST:
        user = get_user_model().objects.get(pk=request.user.person_id)
        user.last_online = datetime.datetime.now(
            timezone.utc)  # At the request of the user, we will update the date and time of the last visit
        user.save(update_fields=['last_online'])
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
    else:
        t = Translate.objects.get(id=1)
        if t.translate == 0:
            lang = ParsingTranslate.open_file(0)
            form_tr = TranslateForm()
            return render(request, 'index.html', {
                'users': Person.objects.all(),
                'form_tr': form_tr,
                'main_news': News.objects.get(id=News.objects.all().count() - 1),
                'second_news': News.objects.get(id=News.objects.all().count() - 2),
                'right_news': News.objects.all()[News.objects.all().count() - 7:News.objects.all().count() - 3],
                "NameApp": lang["NameApp"],
                "Bank": lang["Bank"],
                "cNews": lang["cNews"],
                "News": lang["News"],
                "Task": lang["Task"],
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
                "cEvent": lang["cEvent"],
                "RequestPullOrg": lang["RequestPullOrg"],
            })
        else:
            lang = ParsingTranslate.open_file(1)
            form_tr = TranslateForm()
            return render(request, 'index.html', {
                'users': Person.objects.all(),
                'form_tr': form_tr,
                'main_news': News.objects.get(id=News.objects.all().count() - 1),
                'second_news': News.objects.get(id=News.objects.all().count() - 2),
                'right_news': News.objects.all()[News.objects.all().count() - 7:News.objects.all().count() - 3],
                'task': Task.objects.all(),
                "NameApp": lang["NameApp"],
                "Bank": lang["Bank"],
                "CreateNews": lang["cNews"],
                "News": lang["News"],
                "oNews": lang["oNews"],
                "Task": lang["Task"],
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
