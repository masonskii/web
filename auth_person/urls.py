from django.urls import path

from auth_person.func import generate_random_string
from auth_person.views import sign_up, is_sign, sign_in, logout_view

app_name = 'login'
"""urlpatterns = [
    path('sign-up {0}/'.format(generate_random_string(19)), sign_up,  name='sign-up'),
    path('sign-in {0}/'.format(generate_random_string(19)), sign_in, name='sign-in'),
    path('user {0}/'.format(generate_random_string(19)), is_sign, name='user-area')
]"""

urlpatterns = [
    path('sign-up/', sign_up,  name='sign-up'),
    path('sign-in/', sign_in, name='sign-in'),
    path('user/', is_sign, name='user-area'),
    path('logout/', logout_view, name='logout')
]