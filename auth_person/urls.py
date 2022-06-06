
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, \
    PasswordResetCompleteView
from django.urls import path, re_path, include

from auth_person.views import sign_up, is_sign, sign_in, logout_view, subsign, go_to_user, show_my_tasks, \
    show_my_events, show_history_request

app_name = 'login'
"""urlpatterns = [
    path('sign-up {0}/'.format(generate_random_string(19)), sign_up,  name='sign-up'),
    path('sign-in {0}/'.format(generate_random_string(19)), sign_in, name='sign-in'),
    path('user {0}/'.format(generate_random_string(19)), is_sign, name='user-area')
]"""

urlpatterns = [
    path('presign/', sign_up, name='presing'),
    path('subsign/', subsign, name='subsign'),
    path('sign-in/', sign_in, name='sign-in'),
    path('user/', is_sign, name='user-area'),
    path('logout/', logout_view, name='logout'),
    path('template/todolist/', show_my_tasks, name='todolist'),
    path('template/myevents/', show_my_events, name='myevents'),
    path('template/history_request/', show_history_request, name='history_req'),
    #re_path(r'^personApi/(?P<login>\D+)/', SignInView.as_view(), name='pApi'),
    re_path(r'^user(?P<id>\d+)/', go_to_user, name='another-user'),

    re_path(r'^reset-password/$', PasswordResetView.as_view(), name='password_reset'),
    re_path(r'^reset-password/done/$', PasswordResetDoneView.as_view(), name='password_reset_done'),

    re_path(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'),

    re_path(r'^reset-password/complete/$', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
