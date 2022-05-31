from django.db.models import Max
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from auth_person.models import Person
from news.models import News


def create_news(request):
    usr = Person.objects.get(person_id=request.user.person_id)
    if request.method == 'POST':
        old_news = News.objects.order_by('id')
        if old_news.count() <= 1:
            new_news = News(
                title=request.POST.get('title'),
                author=usr.username,
                img=request.FILES[
                    'file'
                ],
                category=request.POST['category'],
                type=request.POST['type'],
                content=request.POST.get('content')
            )
            new_news.save()
            return redirect(reverse('index'))
        else:
            for item in old_news[1:(News.objects.all().count() - 1)]:
                item.__class__.objects.update(is_actual=False)
            new_news = News(
                title=request.POST.get('title'),
                author=usr.username,
                img=request.FILES[
                    'file'
                ],
                category=request.POST['category'],
                type=request.POST['type'],
                content=request.POST.get('content')
            )
            new_news.save()
            return redirect(reverse('index'))
    else:
        return render(request, 'create_news.html')


def show_news(request):
    return render(request,
           'news.html',
           {
               'main_news': News.objects.get(id=News.objects.all().count() - 1),
               'second_news': News.objects.get(id=News.objects.all().count() - 2),
               'right_news': News.objects.all()[News.objects.all().count() - 7:News.objects.all().count() - 3],
               'sport_news': News.objects.filter(category='sport'),
               'tech_news': News.objects.filter(category='technology'),
               'buss_news': News.objects.filter(category='business'),
               'ent_news': News.objects.filter(category='entertainment'),
               'feat_news': News.objects.filter(category='feature'),
               'popular_news': News.objects.filter(count_like=6),
               'lates_news': News.objects.filter(date='2022-05-31'),
               'viewed_news': News.objects.filter(count_like=6),
               'read_news': News.objects.filter(count_like=6),
               'recent_news': News.objects.filter(count_like=6),
               'another_news': News.objects.all()[:9]
           })
