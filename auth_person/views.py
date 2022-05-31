from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
import datetime
# Create your views here.
from django.urls import reverse

from auth_person.consts import DEFAULT_ROLE, ORG_ROLE
from auth_person.forms import PersonRegistrationForms, SignIn
from auth_person.func import generated_card
from auth_person.models import Person, Organization, Role
from django.contrib.auth.models import User

from consts import DEFAULT_NAME_APP, DEFAULT_START_BALANCE
from my_pull_request.forms import FormsOrgPullRequest, FormsMakesPullRequest
from my_pull_request.models import OrgPullRequest, PersonPullRequest


def subsign(request):
    if request.method == 'POST':
        new_user = Person.objects.get(person_id=request.user.person_id)
        new_user.name = request.POST['name']
        new_user.surname = request.POST['surname']
        new_user.ndName = request.POST['ndName']
        new_user.birthday = request.POST['birthday']
        new_user.logo = request.FILES['logo']
        new_user.phone = request.POST['phone']
        new_user.country = request.POST['country']
        new_user.address = request.POST['address']
        new_user.sex = request.POST['gender']
        new_user.save()
        Person.objects.update(name=new_user.name, surname=new_user.surname)
        return redirect(reverse('login:user-area'),
                        kwargs={'user': Person.objects.get(person_id=request.user.person_id)})
    return render(
        request,
        'subsign.html',

    )


def sign_up(request):
    if 'send_person' in request.POST:
        new_person = PersonRegistrationForms(request.POST)
        if new_person.is_valid():
            role = Role(role=DEFAULT_ROLE)
            role.save()
            user = Person.objects.create_user(username=new_person.cleaned_data['login'],
                                              email=new_person.cleaned_data['email'],
                                              password=new_person.cleaned_data['password'],
                                              balance=DEFAULT_START_BALANCE,
                                              role=role,
                                              card=generated_card(),
                                              bio='user',
                                              translate=0,

                                              )
            user.save()
            # request_user = authenticate(username=new_person.cleaned_data['login'],
            #                           password=new_person.cleaned_data['password']))
            login(request, user)
            return redirect(reverse('login:subsign'), kwargs={'user': user})
    else:
        return render(
            request,
            'registration.html',
        )


def sign_in(request):
    if request.method == 'POST':
        pas = request.POST['password']
        usr = Person.objects.get(username=request.POST['login'])
        if not usr.check_password(pas):
            return render(
                request,
                'invData.html'
            )
        # request_user = authenticate(username=usr.username, password=usr.password)
        # if request_user is not None and request_user.is_active:
        login(request, usr)
        return redirect(reverse('index'), {'user': usr})

    else:
        form_sign = SignIn()
        return render(
            request,
            'sign.html',
            {
                'form': form_sign,
                'title': DEFAULT_NAME_APP
            }
        )


def is_sign(request):
    if 'succ_req' in request.POST:
        rqst = OrgPullRequest.objects.get(id=request.POST.get('id_req'))
        person = Person.objects.get(phone=rqst.person_telephone,
                                    email=rqst.person_email)
        person.is_organizate = True
        r = Role.objects.create(role='organizated')
        r.save()
        person.role = r
        person.save()
        Organization.objects.create(
            name=rqst.name_org,
            type=rqst.type_org,
            logo=rqst.logo_org,
            address=rqst.address,
            description=rqst.description,
            user=person,
        ).save()
        rqst.delete()
        return HttpResponseRedirect('/')
    if 'not_succ_req' in request.POST:
        rqst = OrgPullRequest.objects.get(id=request.POST.get('id_req'))
        rqst.delete()
        return HttpResponseRedirect('/')
    if 'added_logo' in request.POST:
        data = request.FILES['logo']
        user = Person.objects.get(person_id=request.user.person_id)
        user.logo = data
        user.save()
        return redirect(reverse('login:user-area'))
    if 'added_name' in request.POST:
        data = request.POST['name']
        user = Person.objects.get(person_id=request.user.person_id)
        user.name = data
        user.save()
        return redirect(reverse('login:user-area'))
    if 'added_surname' in request.POST:
        data = request.POST['surname']
        user = Person.objects.get(person_id=request.user.person_id)
        user.surname = data
        user.save()
        return redirect(reverse('login:user-area'))
    if 'added_ndName' in request.POST:
        data = request.POST['ndName']
        user = Person.objects.get(person_id=request.user.person_id)
        user.ndName = data
        user.save()
        return redirect(reverse('login:user-area'))
    if 'added_phone' in request.POST:
        data = request.POST['phone']
        user = Person.objects.get(person_id=request.user.person_id)
        user.phone = data
        user.save()
        return redirect(reverse('login:user-area'))
    if 'added_birthday' in request.POST:
        data = request.POST['birthday']
        user = Person.objects.get(person_id=request.user.person_id)
        user.birthday = data
        user.save()
        return redirect(reverse('login:user-area'))
    if 'added_country' in request.POST:
        data = request.POST['country']
        user = Person.objects.get(person_id=request.user.person_id)
        user.country = data
        user.save()
        return redirect(reverse('login:user-area'))
    if 'added_address' in request.POST:
        data = request.POST['address']
        user = Person.objects.get(person_id=request.user.person_id)
        user.address = data
        user.save()
        return redirect(reverse('login:user-area'))
    if 'added_sex' in request.POST:
        data = request.POST['sex']
        user = Person.objects.get(person_id=request.user.person_id)
        user.sex = data
        user.save()
        return redirect(reverse('login:user-area'))
    else:
        form = OrgPullRequest.objects.all()
        new_session = Person.objects.get(person_id=request.user.person_id)
        if not new_session:
            return render(
                request,
                'invData.html'
            )
        else:
            return render(
                request,
                'personalArea.html',
                {
                    'form': form,
                    'title': DEFAULT_NAME_APP,
                    'person': new_session,
                }
            )


def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")
