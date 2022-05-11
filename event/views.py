from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from auth_person.models import Person
from event.models import Task


def created_task(request):
    if request.method == 'POST':
        new_task = Task(
            implementerId=Person.objects.get(person_id=request.user.person_id),
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            taskData=request.POST.get('file'),
            payment=request.POST.get('payment'),
            startDate=request.POST.get('start_date'),
            finishDate=request.POST.get('finish_date')
        )
        new_task.save()
        return redirect(reverse('index'),
                        kwargs={'task': Task.objects.all()})
    else:
        return render(request, 'create_task.html')
