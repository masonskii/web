from django.urls import re_path, path

from auth_person.views import registration, signUp

urlpatterns = [
    path('sign_up/', registration),
    path('sign_in/', signUp)
    #re_path(r'^personalArea/(?P<name>\D+)/(?P<id>\d+)', is_sign)
]