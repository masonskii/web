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
        if decimal.Decimal(self.summary) <= 0:
            return False
        self.amout = decimal.Decimal(self.summary)
        self.person = Person.objects.get(person_id=self.senderId.person_id)
        self.rec_pers = Person.objects.get(person_id=self.recipientId.person_id)
        if self.amout > self.person.balance:
            return False
        if self.person.balance - self.amout < 0:
            return False
        self.person.balance = self.person.balance - self.amout
        self.rec_pers.balance = self.rec_pers.balance + self.amout
        self.person.save()
        self.rec_pers.save()
        return True

