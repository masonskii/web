from auth_person.models import Person, Role, Logo, Email, MobilePhone
from .consts import *


def create_new_user(request):
    new_user = Person()
    new_user.login = request.POST.get('login')
    new_user.password = request.POST.get('password')
    new_user.name = request.POST.get('name')
    new_user.surname = request.POST.get('surname')
    new_user.birthday = request.POST.get('birthday')
    new_user.balance = 0.0
    new_user.roleId = add_to_user_role()
    new_user.logoId = add_to_user_logo(request)
    new_user.email = add_to_user_email(request)
    new_user.phone = add_to_user_phone(request)
    new_user.save()
    return new_user


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
