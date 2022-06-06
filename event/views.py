import datetime

from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from auth_person.models import Person
from event.models import Task, Event, GoingEvent


def created_task(request):
    if request.method == 'POST':
        new_task = Task(
            implementerId=Person.objects.get(person_id=request.user.person_id),
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            taskData=request.FILES.get('file'),
            payment=request.POST.get('payment'),
            startDate=request.POST.get('start_date'),
            finishDate=request.POST.get('finish_date'),
            priority=request.POST.get('priority')
        )
        new_task.save()
        return redirect(reverse('index'),
                        kwargs={'task': Task.objects.all()})
    else:
        return render(request, 'create_task.html')


def created_event(request):
    if request.method == 'POST':
        caster = Person.objects.get(person_id=request.POST['caster'][0])
        Event.objects.create(
            title=request.POST['title'],
            startDate=request.POST['start_date'],
            finishDate=request.POST['finish_date'],
            startTime=request.POST['start_time'],
            duration=request.POST['duration'],
            location=request.POST['location'],
            caster=caster,
            description=request.POST['description'],
            img=request.FILES['file']
        ).save()
        return redirect(reverse('index'))
    else:
        return render(request, 'create_events.html', {'casters': Person.objects.filter(is_organizate=True)})


def show_task(request):
    if request.method == 'POST':
        pass
    if 'going' in request.POST:
        task = Task.objects.get(id=request.POST['id'])
        task.customerId = Person.objects.get(person_id=request.user.person_id)
        task.save()
        return render(request,
                      'task.html',
                      {
                       'tasks': Task.objects.all(),
                       'return': True
                       })
    else:
        return render(
            request,
            'task.html',
            {
             'tasks': Task.objects.all()
             }
        )


def show_event(request):
    if request.method == 'POST':
        pass
    if 'going' in request.POST:
        GoingEvent.objects.create(
            id_event=Event.objects.get(id=request.POST['id']),
            id_person=Person.objects.get(person_id=request.user.person_id)
        ).save()
        return render(request,
                      'event.html',
                      {'Today': 'Сегодня',
                       'Tomorrow': 'Завтра',
                       'Day_after_tomorrow': 'Послезавтра',
                       'today_date': datetime.date.today,
                       'tomorrow_date': datetime.date.today() + datetime.timedelta(days=1),
                       'day_after_tomorrow_date': datetime.date.today() + datetime.timedelta(days=2),
                       'events': Event.objects.all(),
                       'return': True
                       })
    else:
        return render(
            request,
            'event.html',
            {'Today': 'Сегодня',
             'Tomorrow': 'Завтра',
             'Day_after_tomorrow': 'Послезавтра',
             'today_date': datetime.date.today,
             'tomorrow_date': datetime.date.today() + datetime.timedelta(days=1),
             'day_after_tomorrow_date': datetime.date.today() + datetime.timedelta(days=2),
             'events': Event.objects.all()
             }
        )


"""def show_event(request, id_event=Event.objects.get(id=Event.objects.all().count - 1)):
    if request.method == 'POST':
        pass
    else:
        return render(
            request,
            'event.html'
        )
"""
