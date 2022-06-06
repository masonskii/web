# Laboratory Inc 
# FabLab Polytech

[![Build Status](https://app.travis-ci.com/masonskii/web.svg?branch=AC)](https://app.travis-ci.com/masonskii/web)

Веб приложение Laboratory Inc (FabLab Polytech) - это микросервисное приложение с открытым исходным кодом, 
позволяющее облегчить и улучшить бытовую жизнь каждого резидента и организатора путем: 

- Автономности
- Автоматизации процессов 
- Бронирования, записи
- ✨Magic ✨

## В ближайших планах:

- Новое API, поспособствующее улучшению производительности и информативности
- Совершенствование дизайна приложения
- Реализация совместимости приложения с API: ВКонтакте, GitHub, Leaderid и т.д. 
- Текстовый редактор прямо у вас в личном кабинете
- ✨И многое многое другое ✨


> Основная цель приложения автоматизировать бытовую жизнь каждого фаблабовца
> и облегчить работу организаторам путем создания единой цифровой платформы


## Техническая часть

Laboratory Inc использует следующий набор фреймворков:

- [Django] - Python framework for web apps!
- [Django Rest Framework] - Framework for creating your own API
- [JQuery] -a set of JavaScript features that focuses on the interaction between JavaScript and HTML.
- [docxtpl] - Powerful and simple package for creating documents based on Python.
- [Pillow] - PIL is the Python Imaging Library by Fredrik Lundh and Contributors
- [Boostrap] - Powerful, extensible, and feature-packed frontend toolkit.

Laboratory Inc имеет открытый исходный код, который можно найти тут -> [GitHub][dill].

## Установка и запуск 
В данный момент веб-приложение Laboratory Inc не находится на хостинге и может быть запущено только в локальной сети.

Для запуска Laboratory Inc требуется: [Python] v 3.9.6+
Для корректной работу так же нужны следующие пакеты:
-[Django](https://www.djangoproject.com/) v4.0.5+.
-[Django Rest Framework] v3.13.1+
-[Pillow] v8.3.1+
-[JQuery] current version
-[docxtpl] v 0.15.2+

**При запуске могут потребоваться дополнительные пакеты, проверяйте текущую версию на [GitHub][dill]**

>Для установки нужного пакета введите в консоли
> ```sh
> $ pip3 intall <package_name>
>```

>Для запуска локального сервера введите в консоли
> ```sh
> $ python manage.py runserver
>```

## Плагины

Laboratory Inc в настоящее время расширен следующими пакетами.
Инструкция по их использованию в их собственных репозиториях

| Plugin | README |
| ------ | ------ |
| GitHub | [plugins/github/README.md][PlGh] |


## Лицензия

MIT

**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)
   [Python]: <https://www.python.org/>
   [dill]: <https://github.com/masonskii/web>
   [git-repo-url]: <https://github.com/masonskii/web.git>
   [Django]: <https://www.djangoproject.com/>
   [Pillow]: <https://pillow.readthedocs.io/en/stable/>
   [Boostrap]: <https://getbootstrap.com/>
   [Django Rest Framework]: <https://www.django-rest-framework.org/>
   [docxtpl]: <https://pypi.org/project/docxtpl/>
   [jQuery]: <http://jquery.com>
