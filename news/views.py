from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from auth_person.models import Person
from news.models import News


def create_news(request):
    usr = Person.objects.get(person_id=request.user.person_id)
    if request.method == 'POST':
        old_news = News.objects.order_by('id')
        for item in old_news[1:(News.objects.all().count()-1)]:
            item.__class__.objects.update(is_actual=False)
        new_news = News(
            title=request.POST.get('title'),
            author=usr.name.name,
            content=request.POST.get('content')
        )
        new_news.save()
        return redirect(reverse('index'),
                        kwargs={'news': News.objects.get(is_actual=True),
                                'old_news': old_news})
    else:
        return render(request, 'create_news.html')
