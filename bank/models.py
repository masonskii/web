import decimal

from django.db import models

# Create your models here.
from auth_person.models import Person


class Transfer(models.Model):
    senderId = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name='Sender'
    )
    recipientId = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name='Recipient'
    )
    summary = models.DecimalField(
        max_digits=19, decimal_places=10
    )
    tDate = models.DateTimeField()

    def sending(self):
        self.amout = decimal.Decimal(self.summary)
        if self.amout <= 0 or self.senderId.balance <= 0 or self.senderId.balance < self.amout:
            return [
                False,
                None,
                None,
                None,
                'Funds sent successfully'
            ]
        self.senderId.balance - self.amout
        self.recipientId.balance + self.amout
        self.senderId.save()
        self.recipientId.save()
        return [
            True,
            self.amout,
            self.senderId.balance,
            self.recipientId.balance,
            'Funds sent successfully'
        ]
