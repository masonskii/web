import random
import string

from auth_person.consts import DEFAULT_ROLE
from auth_person.models import Role, Logo, Email, MobilePhone, PersonCard, PersonLogin, PersonPassword, Person, \
    PersonName, PersonSurname, PersonNdName, PersonBirthday
from consts import START_NUMBER_CARD, DEFAULT_START_BALANCE


class CreateNewUser:

    def __init__(self, request):
        self.request = request
        self.new_password = PersonPassword()
        self.new_login = PersonLogin()
        self.new_user = Person()
        self.new_email = Email()
        self.new_role = Role()
        self.new_card = PersonCard()
        self.generate = GenerateCard()

    def main_create_new_user(self):
        self.new_login.login = self.request.POST.get('login')
        self.new_password.password = self.request.POST.get('password')
        self.new_email.email = self.request.POST.get('email')
        self.new_role.role = DEFAULT_ROLE
        self.new_card.number = self.generate.number
        self.new_card.secret_code = self.generate.secret_code
        self.new_login.save()
        self.new_password.save()
        self.new_email.save()
        self.new_role.save()
        self.new_card.save()
        self.new_user.login = self.new_login
        self.new_user.password = self.new_password
        self.new_user.email = self.new_email
        self.new_user.roleId = self.new_role
        self.new_user.card = self.new_card
        self.new_user.balance = DEFAULT_START_BALANCE
        self.new_user.save()


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
    return '{0}{1}{2}{3} {4}{5}{6}{7}'.format(random.randint(0, 9),
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
        number = '{0} {1}'.format(START_NUMBER_CARD, generate_number_card())
        return number

    def __reinit__(self):
        self.number, self.secret_code = self.generate_number(), generate_secret_code()
