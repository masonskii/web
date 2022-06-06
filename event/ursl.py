from django.urls import path, re_path

from event.views import created_task, show_event, created_event, show_task

app_name = 'events'
"""urlpatterns = [
    path('sign-up {0}/'.format(generate_random_string(19)), sign_up,  name='sign-up'),
    path('sign-in {0}/'.format(generate_random_string(19)), sign_in, name='sign-in'),
    path('user {0}/'.format(generate_random_string(19)), is_sign, name='user-area')
]"""

urlpatterns = [
    path('createTask/', created_task, name='create_task'),
    path('createEvent/', created_event, name='create_event'),
    path('event/', show_event, name='show_event'),
    path('task/', show_task, name='show_task'),
    #re_path(r'^events/event(?P<id>\d+)', show_event, name='event_show'),
]