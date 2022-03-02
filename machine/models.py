from django.db import models

# Create your models here.
"""class Machine(models.Model):
    title = models.CharField(max_length=30)
    pas = models.BooleanField(default=False)
    booking = models.BooleanField(default=False)
    costPerHour = models.DecimalField(max_digits=19, decimal_places=10)

"""

"""
class MachineBooking(models.Model):
    MachineId = models.ForeignKey(
        Machine,
        on_delete=models.CASCADE,
        related_name='MachineBookingMachineId'
    )
    customerId = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name='MachineBookingPersonId'
    )
    startTime = models.TimeField(

    )
    endTime = models.TimeField(

    )
    bookingData = models.DateField(

    )"""
