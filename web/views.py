from django.http import HttpResponse
from django.shortcuts import render

from consts import DEFAULT_NAME_APP


def index(request):
    return render(
        request,
        'index.html',
)

