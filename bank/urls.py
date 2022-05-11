from django.urls import path

from auth_person.func import generate_random_string
from bank.views import transfer, successfully_transaction, error_transaction

app_name = 'bank'
urlpatterns = [
    path('transaction/', transfer,  name='transfer'),
    path('result?transaction#{0}/'.format(generate_random_string(6)), successfully_transaction, name='sc-transact'),
    path('result?transaction#{0}/'.format(generate_random_string(6)), error_transaction, name='err-transact'),
]