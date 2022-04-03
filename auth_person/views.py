from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
import datetime
# Create your views here.
from django.urls import reverse

from auth_person.forms import PersonRegistrationForms, SignIn, PersonSubSignForm
from auth_person.func import add_to_user_role, add_to_user_logo, \
    add_to_user_phone, GenerateCard, add_to_user_card, add_login, add_password, add_email
from auth_person.models import Person
from django.contrib.auth.models import User

from consts import DEFAULT_NAME_APP, DEFAULT_START_BALANCE


def subsign(request):
    return render(
        request,
        'subsign.html',
    )


def sign_up(request):
    if request.method == 'POST':
        new_person = PersonRegistrationForms(request.POST)
        if new_person.is_valid():
            new_user = Person()
            new_user.login = add_login(request.POST.get('login'))
            new_user.password = add_password(request.POST.get('password'))
            new_user.email = add_email(request.POST.get('email'))
            new_user.balance = 0.0
            new_user.roleId = add_to_user_role()
            new_user.card = add_to_user_card()
            new_user.save()
            finally_user = User.objects.create_user(username=new_user.login.login,
                                                    email=new_user.email.email,
                                                    password=new_user.password.password
                                                    )
            finally_user.save()
            request_user = authenticate(username=new_user.login.login, password=new_user.password.password)
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
    new_session = Person.objects.get(login=request.user.username)
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
                'title': DEFAULT_NAME_APP,
                'person': new_session,
                'logo_obj': new_session.logoId.logo.url
            }
        )


def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")
