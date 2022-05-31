from django.urls import path

from market.views import sell

app_name = 'market'
urlpatterns = [
    path('buy/', sell,  name='sell'),
]