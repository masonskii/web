import mimetypes
import os
from wsgiref.util import FileWrapper

from django.http import StreamingHttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from auth_person.models import PersonCard, Person
from bank.forms import TransferForms
from bank.func import search_person, sender, create_document_transaction
from bank.models import Transfer
from web.settings import MEDIA_URL, MEDIA_ROOT


def transfer(request):
    if 'send_transaction' in request.POST:
        tr = Transfer()
        tr.senderId = sender(request.user)
        if not tr.senderId:
            return render(
                request, 'invData.html'
            )
        else:
            tr.recipientId = search_person(request.POST.get('number'))
            tr.summary = request.POST.get('summary')
            res = tr.sending()
            if res:
                tr.save()
                return redirect(reverse('bank:sc-transact'), kwargs={'tr': res})
            else:
                return redirect(reverse('bank:err-transact'), kwargs={'tr': res})
    if 'transaction' in request.POST:
        sName = request.POST.get('sender_name'), request.POST.get('sender_surname')
        rName = request.POST.get('recip_name'), request.POST.get('recip_surname')
        sum = request.POST.get('summary')
        tDate = request.POST.get('tDate')

        response = create_document_transaction(sName, rName, tDate, sum)
        return response
    else:
        history_transfer = Transfer.objects.filter(senderId=request.user.id)

        return render(request, 'transfer.html', {'person_tr': history_transfer})


def successfully_transaction(request):
    return render(request, 'result_transaction.html')


def error_transaction(request):
    return render(request, 'error_transaction.html')
































