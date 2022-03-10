from django.db import models

# Create your models here.


class Role(models.Model):
    role_id = models.AutoField(primary_key=True)
    role = models.CharField(max_length=20)


class Logo(models.Model):
    logo_id = models.AutoField(primary_key=True)
    logo = models.ImageField(upload_to='files/image/user_logo/%Y-%m-%d/', null=True, blank=True)


class Email(models.Model):
    email_id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=50, null=True, blank=True)


class MobilePhone(models.Model):
    mPhone_id = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=12, null=True, blank=True)


class Person(models.Model):
    person_id = models.AutoField(primary_key=True)
    login = models.CharField(max_length=20, null=False, help_text='basic login information', unique=True)
    password = models.CharField(max_length=32, null=False, help_text='basic login information', unique=True)
    name = models.CharField(max_length=30, null=False)
    surname = models.CharField(max_length=30, null=False)
    ndName = models.CharField(max_length=30, null=True, blank=True)
    birthday = models.CharField(max_length=30)
    roleId = models.ForeignKey(
        Role,
        on_delete=models.CASCADE,
    )
    logoId = models.ForeignKey(
        Logo,
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='toLogoFromUser'
    )
    email = models.ForeignKey(
        Email,
        on_delete=models.CASCADE,
        default=10,
        null=True, blank=True,
        related_name='toEmailFromUser'
    )
    phone = models.ForeignKey(
        MobilePhone,
        on_delete=models.CASCADE,
        default=10,
        null=True, blank=True,
        related_name='toPhoneFromUser'
    )
    balance = models.DecimalField(max_digits=19, decimal_places=10)
    registrationDate = models.DateTimeField(auto_now=True)
    lastEntrance = models.DateTimeField(auto_now=True)


class Department(models.Model):
    departmen_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, null=False)


class Specialization(models.Model):
    specialization_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20, null=False)


class PersonSpecs(models.Model):
    personSpecs_id = models.AutoField(primary_key=True)
    SpecId = models.ForeignKey(
        Specialization,
        on_delete=models.CASCADE,
        related_name='PersonSpecsSpecId'
    )
    PersonId = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name='PersonSpecsPersonId'
    )


class Membership(models.Model):
    membership_id = models.AutoField(primary_key=True)
    DepartmentId = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='MembershipDepartmentId'
    )
    PersonId = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name='MembershipPersonId'
    )
