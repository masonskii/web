from django.shortcuts import render
from auth_person.models import Person
from consts import DEFAULT_NAME_APP


def index(request):
        return render(request, 'index.html')
