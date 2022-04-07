from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
import datetime
# Create your views here.
from django.urls import reverse

from auth_person.forms import PersonRegistrationForms, SignIn
from auth_person.func import CreateNewUser
from auth_person.models import Person, PersonLogin, PersonPassword, PersonName, PersonSurname, PersonNdName, \
    PersonBirthday, MobilePhone, Logo
from django.contrib.auth.models import User

from consts import DEFAULT_NAME_APP, DEFAULT_START_BALANCE


def subsign(request):
    if request.method == 'POST':
            new_user = Person.objects.get(person_id=request.user.id)
            name = PersonName()
            surname = PersonSurname()
            ndName = PersonNdName()
            birthday = PersonBirthday()
            new_phone = MobilePhone()
            new_logo = Logo()
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
            return redirect(reverse('login:user-area'), kwargs={'user': Person.objects.get(person_id=request.user.id)})
    return render(
        request,
        'subsign.html',
    )


def sign_up(request):
    if request.method == 'POST':
        new_person = PersonRegistrationForms(request.POST)
        if new_person.is_valid():
            new_user = CreateNewUser(request)
            new_user.main_create_new_user()
            finally_user = User.objects.create_user(username=request.POST.get('login'),
                                                    email=request.POST.get('email'),
                                                    password=request.POST.get('password')
                                                    )
            finally_user.save()
            request_user = authenticate(username=request.POST.get('login'), password=request.POST.get('password'))
            if request_user is not None:
                login(request, request_user)
                return redirect(reverse('login:subsign'), kwargs={'user': request_user})
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
            pas = PersonPassword.objects.filter(password=request.POST.get('password'))
            for i in range(len(pas)):
                try:
                    session_complited = Person.objects.get(login=log.login_id, password=pas[i].password_id)
                    if session_complited is not None:
                        session_complited.__class__.objects.update(lastEntrance=datetime.date.today())
                        request_user = authenticate(username=session_complited.login.login,
                                                    password=session_complited.password.password)
                        if request_user is not None:
                            login(request, request_user)
                            return redirect(reverse('index'), kwargs={'user': request_user})
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
    new_session = Person.objects.get(person_id=request.user.id)
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
