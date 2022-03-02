from django.shortcuts import render

# Create your views here.
from auth_person.models import Person


def main(request):
    return render(request, 'main.html', {'title': 'Главная страница', 'data_context': 'Hello'})
