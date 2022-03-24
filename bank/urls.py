from django.urls import path

from bank.views import transfer

app_name = 'bank'
urlpatterns = [
    path('transaction/', transfer,  name='transfer'),
]