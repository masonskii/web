from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from auth_person.models import Person, Role, Logo, Email, MobilePhone

from .consts import *


def add_to_user_role():
    new_role = Role()
    new_role.role = DEFAULT_ROLE
    new_role.save()
    return new_role


def add_to_user_logo(request):
    new_logo = Logo()
    new_logo.logo = request.FILES.get('logo')
    new_logo.save()
    return new_logo


def add_to_user_email(request):
    new_email = Email()
    new_email.email = request.POST.get('email')
    new_email.save()
    return new_email


def add_to_user_phone(request):
    new_phone = MobilePhone()
    new_phone.phone = request.POST.get('mobilePhone')
    new_phone.save()
    return new_phone


import random
import string


def generate_random_string(length=15):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string

