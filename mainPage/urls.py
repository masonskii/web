from django.urls import re_path, path, include
from .views import *
urlpatterns = [
    path('', main),
]
