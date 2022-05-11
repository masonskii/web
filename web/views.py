from django.shortcuts import render
from auth_person.models import Person
from consts import DEFAULT_NAME_APP
from event.models import Task
from news.models import News


def index(request):
        return render(request, 'index.html', {
                'news': News.objects.filter(is_actual=True),
                'old_news': News.objects.filter(is_actual=False),
                'task': Task.objects.all()
        })
