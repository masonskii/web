import datetime

from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from auth_person.models import Person
from machine.models import Machine, MachineBooking


def booking(request, id):
    pass


def show_booking(request):
    summary = 0
    var = 0
    obj = 0
    if 'accept-booking' in request.POST:
        var.save()

        return render(
            request,
            'bookingMachine.html',
            {
                'return_sms': True,
                'list': Machine.objects.filter(booking=False),
            }
        )
    if 'query_booking' in request.POST:
        obj = Machine.objects.get(id=request.POST['id'])
        var = MachineBooking.objects.create(
            MachineId=obj,
            customerId=Person.objects.get(person_id=request.user.person_id),
            startTime=request.POST['start_time'],
            bookingDate=request.POST['date'],
            endTime=request.POST['endtime']
        )
        obj.booking = True
        obj.save()
        var.full_clean()
        var.save()
        duration_h = var.period_duration()
        summary = int(obj.costPerHour) * int(duration_h)
        print(int(obj.costPerHour), int(duration_h))

        obj1 = Person.objects.get(person_id=request.user.person_id)
        if summary > obj1.balance:
            return render(
                request,
                'bookingMachine.html',
                {
                    'return_sms': False,
                    'list': Machine.objects.filter(booking=False),
                }
            )
        obj1.balance = obj1.balance - summary
        obj1.save()
        return render(
            request,
            'bookingMachine.html',
            {
                'return_sms': True,
                'list': Machine.objects.filter(booking=False),
            }
        )
    else:
        return render(
            request,
            'bookingMachine.html',
            {'list': Machine.objects.filter(booking=False),'return_sms':None}
        )


def create_m(request):
    if request.method == 'POST':
        Machine.objects.create(
            title=request.POST['title'],
            costPerHour=request.POST['cost'],
            img=request.FILES['file'],
        )
        return redirect(reverse('index'))
    else:
        return render(
            request,
            'create_machine.html'
        )
