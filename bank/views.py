from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from bank.forms import TransferForms
from bank.func import search_person, sender
from bank.models import Transfer


def transfer(request):
    if request.method == 'POST':
        new_transfer = TransferForms(request.POST)
        if new_transfer.is_valid():
            tr = Transfer()
            tr.senderId = sender(request.user)
            if not tr.senderId:
                return render(
                    request, 'invData.html'
                )
            else:
                tr.recipientId = search_person(request.POST.get('name'), request.POST.get('number'))
                tr.summary = request.POST.get('summary')
                if not request.POST.get('comm'):
                    return redirect(reverse('index'), kwargs={'user': request.user})
        else:
            return render(
                request, 'invData.html'
            )
    return render(request, 'transfer.html', {'user': request.user})
