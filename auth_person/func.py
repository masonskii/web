import random
import string

from auth_person.models import Person, Role, Logo, Email, MobilePhone, PersonCard
from consts import START_NUMBER_CARD

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

def add_to_user_card():
    new_card = PersonCard()
    generate = GenerateCard()
    new_card.number = generate.number
    new_card.secret_code = generate.secret_code
    new_card.save()
    return new_card




def generate_random_string(length=15):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string


def generate_alphanum_random_string(length):
    letters_and_digits = string.ascii_letters + string.digits
    rand_string = ''.join(random.sample(letters_and_digits, length))
    return rand_string


def generate_random_string_unique(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.sample(letters, length))
    return rand_string


def generate_number_card():
    return '{0}{1}{2}{3}-{4}{5}{6}{7}'.format(random.randint(0, 9),
                                              random.randint(0, 9),
                                              random.randint(0, 9),
                                              random.randint(0, 9),
                                              random.randint(0, 9),
                                              random.randint(0, 9),
                                              random.randint(0, 9),
                                              random.randint(0, 9),
                                              random.randint(0, 9)
                                              )


def generate_secret_code():
    n1, n2, n3 = random.randint(0, 9), random.randint(0, 9), random.randint(0, 9)
    secret_code = '{0}{1}{2}'.format(n1, n2, n3)
    return secret_code


class GenerateCard:
    def __init__(self):
        self.number = self.generate_number()
        self.secret_code = generate_secret_code()

    def generate_number(self):
        number = '{0}-{1}'.format(START_NUMBER_CARD, generate_number_card())
        return number

    def __reinit__(self):
        self.number, self.secret_code = self.generate_number(), generate_secret_code()