from django.urls import path

from auth_person.func import generate_random_string
from bank.views import transfer

app_name = 'bank'
urlpatterns = [
    path('transaction/', transfer,  name='transfer'),
]