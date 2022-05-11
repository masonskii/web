from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
import datetime
# Create your views here.
from django.urls import reverse

from auth_person.consts import DEFAULT_ROLE, ORG_ROLE
from auth_person.forms import PersonRegistrationForms, SignIn
from auth_person.func import Created, generated_card
from auth_person.models import Person, PersonLogin, PersonName, PersonSurname, PersonNdName, \
    PersonBirthday, MobilePhone, Logo, Email, Role
from django.contrib.auth.models import User

from consts import DEFAULT_NAME_APP, DEFAULT_START_BALANCE


def subsign(request):
    if request.method == 'POST':
        new_user = Person.objects.get(person_id=request.user.person_id)
        name = PersonName()
        surname = PersonSurname()
        ndName = PersonNdName()
        birthday = PersonBirthday()
        new_phone = MobilePhone()
        new_logo = Logo()
        new_bio = request.POST.get('bio')
        name.name = request.POST.get('name')
        surname.surname = request.POST.get('surname')
        ndName.ndName = request.POST.get('ndName')
        birthday.birthday = request.POST.get('birthday')
        new_phone.phone = request.POST.get('phone')
        new_logo.logo = request.FILES.get('logo')
        name.save()
        surname.save()
        ndName.save()
        birthday.save()
        new_phone.save()
        new_logo.save()
        new_user.name = name
        new_user.surname = surname
        new_user.ndName = ndName
        new_user.birthday = birthday
        new_user.phone = new_phone
        new_user.logoId = new_logo
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
            username = PersonLogin(login=request.POST.get('login'))
            email = Email(email=request.POST.get('email'))
            role = Role(role=DEFAULT_ROLE)
            role.save()
            username.save()
            email.save()
            user = Person.objects.create_user(username=username,
                                              email=email,
                                              password=request.POST.get('password'),
                                              balance=DEFAULT_START_BALANCE,
                                              roleId=role,
                                              card=generated_card(),
                                              bio='user'
                                              )
            user.save()
            # request_user = authenticate(username__login=request.POST.get('login'))
            login(request, user)
            return redirect(reverse('login:subsign'), kwargs={'user': user})
    if 'send_org' in request.POST:
        new_person = PersonRegistrationForms(request.POST)
        if new_person.is_valid():
            username = PersonLogin(login=request.POST.get('login'))
            email = Email(email=request.POST.get('email'))
            role = Role(role=ORG_ROLE)
            role.save()
            username.save()
            email.save()
            user = Person.objects.create_user(username=username,
                                              email=email,
                                              password=request.POST.get('password'),
                                              balance=DEFAULT_START_BALANCE,
                                              roleId=role,
                                              card=generated_card(),
                                              bio='organizate',
                                              is_organizate=True,
                                              organization_name=request.POST.get('org_name'),
                                              type_activity=request.POST.get('type')
                                              )
            user.save()
            # request_user = authenticate(username__login=request.POST.get('login'))
            login(request, user)
            return redirect(reverse('login:subsign'), kwargs={'user': user})
    else:
        return render(
            request,
            'registration.html',
            {
                'title': DEFAULT_NAME_APP
            }
        )


def sign_in(request):
    if request.method == 'POST':
        new_session_sign = SignIn(request.POST)
        if new_session_sign.is_valid():
            log = PersonLogin.objects.get(login=request.POST.get('login'))
            pas = Person.objects.filter(password=request.POST.get('password'))
            for i in range(len(pas)):
                try:
                    session_complited = Person.objects.get(login=log.login_id, password=pas[i].password_id)
                    if session_complited is not None:
                        session_complited.__class__.objects.update(lastEntrance=datetime.date.today())
                        request_user = authenticate(username=session_complited.login.login,
                                                    password=session_complited.password.password)
                        if request_user is not None:
                            login(request, request_user)
                            return redirect(reverse('index'), {'user': session_complited})
                except:
                    continue
            else:
                return render(
                    request,
                    'invData.html'
                )
        else:
            return render(
                request,
                'invData.html'
            )
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
    new_session = Person.objects.get(person_id=request.user.person_id)
    if not new_session:
        return render(
            request,
            'invData.html'
        )
    else:
        if new_session.logoId is None:
            return render(
                request,
                'personalArea.html',
                {
                    'title': DEFAULT_NAME_APP,
                    'person': new_session,
                    'logo_obj': None
                }
            )
        else:
            return render(
                request,
                'personalArea.html',
                {
                    'title': DEFAULT_NAME_APP,
                    'person': new_session,
                    'logo_obj': new_session.logoId.logo.url
                }
            )


def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")
