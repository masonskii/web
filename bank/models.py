import decimal

from django.db import models

# Create your models here.
from auth_person.models import Person


class Transfer(models.Model):
    senderId = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name='sender'
    )
    recipientId = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name='recipient'
    )
    summary = models.DecimalField(
        max_digits=19, decimal_places=10
    )
    tDate = models.DateTimeField(auto_now=True)

    def sending(self):
        if self.senderId.card == self.recipientId.card:
            raise ValueError('senderId.card == recipientId.card')
        if decimal.Decimal(self.summary) <= 0:
            raise ValueError('decimal.Decimal(self.summary) <= 0')
        self.amout = decimal.Decimal(self.summary)
        self.person = Person.objects.get(person_id=self.senderId.person_id)
        self.rec_pers = Person.objects.get(person_id=self.recipientId.person_id)
        if self.amout > self.person.balance:
            raise ValueError('amout > person.balance')
        if self.person.balance - self.amout < 0:
            raise ValueError('person.balance - self.amout  < 0')
        self.person.balance = self.person.balance - self.amout
        self.rec_pers.balance = self.rec_pers.balance + self.amout
        self.person.save(update_fields=['balance'])
        self.rec_pers.save(update_fields=['balance'])
        return True

