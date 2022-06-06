from django.contrib.auth import login, authenticate, logout, get_user_model
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
import datetime
# Create your views here.
from django.urls import reverse
from rest_framework import status
from rest_framework.decorators import renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from auth_person.consts import DEFAULT_ROLE, ORG_ROLE
from auth_person.forms import PersonRegistrationForms, SignIn
from auth_person.func import generated_card, download_file
from auth_person.models import Person, Organization, Role, Comm
from django.contrib.auth.models import User

from consts import DEFAULT_NAME_APP, DEFAULT_START_BALANCE
from event.models import GoingEvent, Event, Task
from my_pull_request.forms import FormsOrgPullRequest, FormsMakesPullRequest
from my_pull_request.models import OrgPullRequest, PersonPullRequest
from _pickle import loads, dumps

now = datetime.datetime.now(datetime.timezone.utc)


"""class SignInVie(APIView):
    @renderer_classes([JSONRenderer])
    def get(self, request, login, password, password_confirm):
        if password != password_confirm:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"Error": {"msg": "Пароли не совпадают"}})
        else:
            user = Person.objectsz"""


def subsign(request):
    if request.method == 'POST':
        new_user = Person.objects.get(person_id=request.user.person_id)
        new_user.name = request.POST['name']
        new_user.surname = request.POST['surname']
        new_user.ndName = request.POST['ndName']
        new_user.birthday = request.POST['birthday']
        new_user.logo = request.FILES['logo']
        new_user.skills = request.POST['skills']
        new_user.phone = request.POST['phone']
        new_user.country = request.POST['country']
        new_user.address = request.POST['address']
        new_user.sex = request.POST['gender']
        new_user.specialization = request.POST['spec']
        new_user.save(
            update_fields=['name', 'surname', 'ndName', 'birthday', 'logo', 'skills', 'phone', 'country', 'address',
                           'sex', 'specialization'])
        user = get_user_model().objects.get(pk=request.user.person_id)
        user.last_online = datetime.datetime.now(
            datetime.timezone.utc)  # At the request of the user, we will update the date and time of the last visit
        user.save(update_fields=['last_online'])
        return redirect(reverse('login:user-area'),
                        kwargs={'user': Person.objects.get(person_id=request.user.person_id)})
    else:
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
            org = Organization.objects.create(
                name=0,
                type=0,
                description=0,
                logo=0,
                address_org=0,
            )
            org.save()
            user = Person.objects.create(username=new_person.cleaned_data['login'],
                                         email=new_person.cleaned_data['email'],
                                         password=new_person.cleaned_data['password'],
                                         balance=DEFAULT_START_BALANCE,
                                         role=role,
                                         card=generated_card(),
                                         bio='user',
                                         translate=0,
                                         organizated_id=org.id,
                                         )
            user.save()
            # request_user = authenticate(username=new_person.cleaned_data['login'],
            #                           password=new_person.cleaned_data['password']))
            login(request, user)
            user = get_user_model().objects.get(pk=request.user.person_id)
            user.last_online = datetime.datetime.now(
                datetime.timezone.utc)  # At the request of the user, we will update the date and time of the last visit
            user.save(update_fields=['last_online'])
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
        if usr.check_password(pas):
            login(request, usr)
            user = get_user_model().objects.get(pk=request.user.person_id)
            user.last_online = datetime.datetime.now(
                datetime.timezone.utc)  # At the request of the user, we will update the date and time of the last visit
            user.save(update_fields=['last_online'])
            return redirect(reverse('index'), {'user': usr})
        # request_user = authenticate(username=usr.username, password=usr.password)
        # if request_user is not None and request_user.is_active:
        else:
            usr = Person.objects.get(username=request.POST['login'], password=pas)
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
    if 'added_info_org' in request.POST:
        Organization.objects.create(
            name=request.POST['reg_org_name'],
            address=request.POST['reg_org_address'],
            type=request.POST['reg_org_type'],
            logo=request.FILES['reg_org_logo'],
            description=request.POST['reg_org_description']
        ).save()
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
                    'title': DEFAULT_NAME_APP,
                    'person': Person.objects.get(person_id=request.user.person_id),
                    'list': Comm.objects.filter(recipient=request.user.person_id),
                }
            )


def go_to_user(request, id):
    a = Person.objects.get(person_id=id)
    user = 0
    try:
        user = request.user.person_id
    except:
        return render(
            request,
            'another_lk.html',
            {
                'title': DEFAULT_NAME_APP,
                'person': Person.objects.get(person_id=id),
                'list': Comm.objects.filter(recipient=id),
            }
        )
    if a.person_id == user:
        form = OrgPullRequest.objects.all()
        new_session = Person.objects.get(person_id=request.user.person_id)
        return render(
            request,
            'personalArea.html',
            {
                'form': form,
                'title': DEFAULT_NAME_APP,
                'person': new_session,
                'events': GoingEvent.objects.filter(id_person=request.user.person_id),
                'list': Task.objects.filter(customerId=request.user.person_id)
            }
        )
    if 'send_comm' in request.POST:
        new_comm = Comm.objects.create(
            sender=Person.objects.get(person_id=request.user.person_id),
            recipient=Person.objects.get(person_id=id),
            description=request.POST['comment']
        )
        new_comm.save()
        return render(
            request,
            'another_lk.html',
            {
                'title': DEFAULT_NAME_APP,
                'person': Person.objects.get(person_id=id),
                'list': Comm.objects.filter(recipient=id)
            }
        )
    return render(
        request,
        'another_lk.html',
        {
            'title': DEFAULT_NAME_APP,
            'person': Person.objects.get(person_id=id),
            'list': Comm.objects.filter(recipient=id),
        }
    )


def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")


def show_my_events(request):
    if 'not_going' in request.POST:
        GoingEvent.objects.get(id=request.POST['id_event']).delete()
        return redirect(reverse('login:user-area'))
    return render(
        request,
        'template_lk_my_events.html',
        {
            'title': DEFAULT_NAME_APP,
            'person': Person.objects.get(person_id=request.user.person_id),
            'list': GoingEvent.objects.filter(id_person=request.user.person_id),
        }
    )


def show_my_tasks(request):
    if 'accept-item-btn' in request.POST:
        task = Task.objects.get(id=request.POST['id'])
        user = Person.objects.get(person_id=request.user.person_id)
        user.balance = user.balance + task.payment
        user.save(update_fields=['balance'])
        task.delete()
        return redirect(reverse('login:user-area'))
    if 'close-item-btn' in request.POST:
        var = Task.objects.get(id=request.POST['id'])
        var.delete()
        return redirect(reverse('login:user-area'))
    if 'download-item-btn' in request.POST:
        task = Task.objects.get(id=request.POST['id'])
        response = download_file(task.taskData)
        return response
    return render(
        request,
        'template_lk_todolist.html',
        {
            'title': DEFAULT_NAME_APP,
            'person': Person.objects.get(person_id=request.user.person_id),
            'list': Task.objects.filter(customerId=request.user.person_id)
        }
    )


def show_history_request(request):
    if 'succ_req' in request.POST:
        rqst = OrgPullRequest.objects.get(id=request.POST.get('id_req'))
        person = Person.objects.get(phone=rqst.person_telephone,
                                    email=rqst.person_email)
        person.is_organizate = True
        r = Role.objects.create(role='organizated')
        r.save()
        person.role = r
        org = Organization.objects.create(
            name=rqst.name_org,
            type=rqst.type_org,
            logo=rqst.logo_org,
            address_org=rqst.address,
            description=rqst.description,
        )
        org.save()
        person.organizate = org
        person.save()
        rqst.delete()
        return HttpResponseRedirect('/')
    if 'not_succ_req' in request.POST:
        rqst = OrgPullRequest.objects.get(id=request.POST.get('id_req'))
        rqst.delete()
        return HttpResponseRedirect('/')
    return render(
        request,
        'template_lk_history_request_org.html',
        {
            'title': DEFAULT_NAME_APP, 'person': Person.objects.get(person_id=request.user.person_id),

            'list': OrgPullRequest.objects.all()
        }
    )
