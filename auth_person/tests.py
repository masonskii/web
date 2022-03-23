from django.test import TestCase

from auth_person.func import GenerateCard


class TestingCard(TestCase):

    def test_1(self):
        self.card = GenerateCard()
        self.assertEqual(self.card.generate_number(), '9090-6940-9999-9999')
        self.assertEqual(generate_secret_code(), '433')