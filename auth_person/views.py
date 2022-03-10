from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
import datetime
# Create your views here.
from django.urls import reverse

from auth_person.forms import PersonRegistrationForms, SignIn
from auth_person.func import add_to_user_role, add_to_user_logo, \
    add_to_user_email, add_to_user_phone
from auth_person.models import Person
from django.contrib.auth.models import User

from consts import DEFAULT_NAME_APP


def sign_up(request):
    if request.method == 'POST':
        new_person = PersonRegistrationForms(request.POST, request.FILES)
        if new_person.is_valid():
            new_user = Person()
            new_user.login = request.POST.get('login')
            new_user.password = request.POST.get('password')
            new_user.name = request.POST.get('name')
            new_user.surname = request.POST.get('surname')
            new_user.birthday = request.POST.get('birthday')
            new_user.balance = 0.0
            new_user.roleId = add_to_user_role()
            new_user.logoId = add_to_user_logo(request)
            new_user.email = add_to_user_email(request)
            new_user.phone = add_to_user_phone(request)
            new_user.save()
            if not new_user.email.email:
                return new_user
            else:
                finally_user = User.objects.create_user(new_user.login,
                                                        new_user.email.email,
                                                        new_user.password
                                                        )
                finally_user.save()
                request_user = authenticate(username=new_user.login, password=new_user.password)
                if request_user is not None:
                    login(request, request_user)
                    return redirect(reverse('index'), kwargs={'user': request_user})
                else:
                    return render(
                        request,
                        'invData.html'
                    )
    else:
        new_person = PersonRegistrationForms()
        return render(
            request,
            'registration.html',
            {
                'form': new_person,
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
