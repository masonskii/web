from django.urls import path

from machine.views import booking, show_booking, create_m

app_name = 'booking-machine'
"""urlpatterns = [
    path('sign-up {0}/'.format(generate_random_string(19)), sign_up,  name='sign-up'),
    path('sign-in {0}/'.format(generate_random_string(19)), sign_in, name='sign-in'),
    path('user {0}/'.format(generate_random_string(19)), is_sign, name='user-area')
]"""

urlpatterns = [
    path('mach_booking/', show_booking, name='sb'),
    path('booking/b<int:id>', booking, name='sbb'),
    path('create_machine/', create_m, name='cm')
]
