"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include, re_path, path

from event.views import created_task
from news.views import create_news, show_news
from .views import *

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('login/', include('auth_person.urls')),
                  path('bank/', include('bank.urls')),
                  path('', index, name='index'),
                  path('creating_news/', create_news, name='createdNews'),
                  path('news/', show_news, name='show_news'),
                  path('creating_task/', created_task, name='createdTask'),
                  path('rq%org/', include('my_pull_request.urls')),
                  path('marketplace/', include('market.urls'))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# В конце файла:
if settings.DEBUG:
    if settings.MEDIA_ROOT:
        # Эта строка опциональна и будет добавлять url'ы только при DEBUG = True
        urlpatterns += staticfiles_urlpatterns()
