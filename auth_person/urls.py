from django.urls import re_path, path

from auth_person.views import registration

urlpatterns = [
    path('registration/', registration),
    #re_path(r'^personalArea/(?P<name>\D+)/(?P<id>\d+)', is_sign)
]