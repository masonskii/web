from django.db import models

# Create your models here.
"""class Transfer(models.Model):
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


"""