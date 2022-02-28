from django.db import models

# Create your models here.
"""
class Task(models.Model):
    customerId = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name='TaskCustomer'
    )
    implementerId = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name='TaskImplementer'
    )
    title = models.CharField(max_length=20, null=False)
    description = models.CharField(max_length=4000, null=True)
    taskData = models.FileField()
    payment = models.DecimalField(
        max_digits=19, decimal_places=10
    )
    startDate = models.DateField()
    finishDate = models.DateField()
"""
