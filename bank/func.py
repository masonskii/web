import datetime
import mimetypes
import os
import random
import string
from pathlib import Path
from wsgiref.util import FileWrapper

from django.http import StreamingHttpResponse

from auth_person.models import Person, PersonCard
from docxtpl import DocxTemplate

from bank.models import Transfer

BASE_DIR = Path(__file__).resolve().parent.parent


def search_person(number_card):
    card = PersonCard.objects.get(number=number_card)
    user = Person.objects.get(card=card.card_id)
    if not user:
        return None
    else:
        return user



def sender(request_user):
    person = Person.objects.get(person_id=request_user.person_id)
    if not person:
        return None
    else:
        return person


def generate_number():
    return '{0}{1}{2}{3}'.format(random.randint(0, 9),
                                 random.randint(0, 9),
                                 random.randint(0, 9),
                                 random.randint(0, 9),
                                 )


def create_document_transaction(sName, rName, tDate, sum):
    doc = DocxTemplate("{0}\\bank\\documents\\templates\\my_word_template.docx".format(BASE_DIR))
    context = {
        'nt': generate_number(),
        'sName': sName,
        'rName': rName,
        'summary': sum,
        'tDate': tDate,
        'create_docx': datetime.datetime.now()
    }
    doc.render(context)
    txt = create_null_doc()
    doc.save(txt)
    file = txt
    filename = os.path.basename(file)
    chunk_size = 8192
    response = StreamingHttpResponse(FileWrapper(open(file, 'rb'), chunk_size),
                                     content_type=mimetypes.guess_type(file)[0])
    response['Content-Length'] = os.path.getsize(file)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response


def create_null_doc():
    path = '{0}\\media\\files\\generated_transactions\\transaction{1}.docx'.format(BASE_DIR, generate_number())
    f = open('path', 'w', encoding='utf-8')
    f.write('s')
    f.close()
    return path