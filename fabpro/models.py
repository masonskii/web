from django.db import models

# Create your models here.
"""class PersonPasses(models.Model):
    MachineId = models.ForeignKey(
        Machine,
        on_delete=models.CASCADE,
        related_name='PersonPassesMachineId'

    )
    PersonId = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name='PersonPassesPersonId'
    )
"""
"""
class PersonSkills(models.Model):
    FabProId = models.ForeignKey(
        FabPro,
        on_delete=models.CASCADE,
        related_name='PersonSkillsFabProId'
    )
    PersonId = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name='PersonSkillsPersonId'
    )
    Term = models.IntegerField()

"""

"""class FabPro(models.Model):
    title = models.CharField(max_length=30, null=False)
    duration = models.DurationField()
    projects = models.BooleanField(default=False)
    teatherId = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
    )
    machineId = models.ForeignKey(
        Machine,
        null=True,
        on_delete=models.CASCADE,
    )
    active = models.BooleanField(default=False)
"""