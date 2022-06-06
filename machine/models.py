from django.db import models

# Create your models here.
from auth_person.models import Person


class Machine(models.Model):
    title = models.CharField(max_length=30)
    pas = models.BooleanField(default=False)
    booking = models.BooleanField(default=False)
    costPerHour = models.DecimalField(max_digits=19, decimal_places=10)
    img = models.ImageField(upload_to='files/machine_img/%Y-%m-%d/')


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
    bookingDate = models.DateField(

    )

    def period_duration(self):
        """
        Returns the length of the period between
        start_t and end_t, in hours.

        This is precise as long as both values
        have 0 as minute/second.
        """
        return self.endTime.hour - self.startTime.hour
