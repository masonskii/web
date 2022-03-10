from datetime import datetime

from django.test import TestCase

from auth_person.func import add_to_user_role
from .models import Transfer
from auth_person.models import Person


# Create your tests here.


class TransferTestCase(TestCase):
    def setUp(self):
        Person.objects.create(
            login='new_login1',
            password='new_password1',
            name='new_name1',
            surname='new_surname1',
            ndName='new_ndName',
            birthday='2001-04-28',
            roleId=add_to_user_role(),
            email=None,
            phone=None,
            balance=100.00,
        )
        Person.objects.create(
            login='new_login2',
            password='new_password2',
            name='new_name2',
            surname='new_surname2',
            ndName='new_ndName2',
            birthday='2001-04-28',
            roleId=add_to_user_role(),
            email=None,
            phone=None,
            balance=100.00,
        )

    def test_transfer_OK1(self):
        self.transfer = Transfer.objects.create(
            senderId=Person.objects.get(login='new_login1'),
            recipientId=Person.objects.get(login='new_login2'),
            summary=50.00,
            tDate=datetime.today()
        )

        self.assertEqual(self.transfer.sending(), [True, 50.00, 100.00, 100.00, 'Funds sent successfully'])

    def test_transfer_OK2(self):
        self.transfer = Transfer.objects.create(
            senderId=Person.objects.get(login='new_login1'),
            recipientId=Person.objects.get(login='new_login2'),
            summary=100.00,
            tDate=datetime.today()
        )

        self.assertEqual(self.transfer.sending(), [True, 100.00, 100.00, 100.00, 'Funds sent successfully'])

    def test_transfer_error(self):
        self.transfer = Transfer.objects.create(
            senderId=Person.objects.get(login='new_login1'),
            recipientId=Person.objects.get(login='new_login2'),
            summary=99.00,
            tDate=datetime.today()
        )

        self.assertEqual(self.transfer.sending(), [True, 99.00, 100.00, 100.00, 'Funds sent successfully'])
