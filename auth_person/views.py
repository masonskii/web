from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
import datetime
# Create your views here.
from django.urls import reverse

from auth_person.forms import PersonRegistrationForms, SignIn, PersonSubSignForm
from auth_person.func import CreateNewUser
from auth_person.models import Person
from django.contrib.auth.models import User

from consts import DEFAULT_NAME_APP, DEFAULT_START_BALANCE


def subsign(request):
    if request.method == 'POST':
        new_person = PersonRegistrationForms(request.POST)
        if new_person.is_valid():
            new_user = CreateNewUser(request)
            new_user.second_create_new_user(request.user)
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
            user_login, user_password = request.POST.get('login'), request.POST.get('password')
            session_complited = Person.objects.get(login=user_login, password=user_password)
            if not session_complited:
                return render(
                    request,
                    'invData.html'
                )
            else:
                session_complited.__class__.objects.update(lastEntrance=datetime.date.today())
                request_user = authenticate(username=session_complited.login, password=session_complited.password)
                if request_user is not None:
                    login(request, request_user)
                    return redirect(reverse('index'), kwargs={'user': request_user})
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
