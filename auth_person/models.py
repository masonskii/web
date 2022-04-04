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
    email = models.EmailField(max_length=50, null=False, blank=False, unique=True)


class MobilePhone(models.Model):
    mPhone_id = models.AutoField(primary_key=True)
    phone = models.CharField(max_length=12, null=True, blank=True)


class PersonCard(models.Model):
    card_id = models.AutoField(primary_key=True)
    number = models.CharField(max_length=12, unique=True)
    secret_code = models.CharField(max_length=3)


class PersonLogin(models.Model):
    login_id = models.AutoField(primary_key=True)
    login = models.CharField(max_length=20, null=False, blank=False, help_text='basic login information', unique=True)


class PersonPassword(models.Model):
    password_id = models.AutoField(primary_key=True)
    password = models.CharField(max_length=32, null=False, blank=False, help_text='basic login information')


class PersonName(models.Model):
    name_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, null=True, blank=True)


class PersonSurname(models.Model):
    surname_id = models.AutoField(primary_key=True)
    surname = models.CharField(max_length=30, null=True, blank=True)


class PersonNdName(models.Model):
    ndName_id = models.AutoField(primary_key=True)
    ndName = models.CharField(max_length=30, null=True, blank=True)


class PersonBirthday(models.Model):
    birthday_id = models.AutoField(primary_key=True)
    birthday = models.DateField(null=True, blank=True)


class Person(models.Model):
    person_id = models.AutoField(primary_key=True)
    login = models.ForeignKey(
        PersonLogin,
        on_delete=models.CASCADE,
        null=False, blank=False,
        related_name='toLoginFromUser'
    )
    password = models.ForeignKey(
        PersonPassword,
        on_delete=models.CASCADE,
        null=False, blank=False,
        related_name='toPasswordFromUser'

    )
    name = models.ForeignKey(
        PersonName,
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='toNameFromUser'
    )
    surname = models.ForeignKey(
        PersonSurname,
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='toSurnameFromUser'
    )
    ndName = models.ForeignKey(
        PersonNdName,
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='toNdNameFromUser'
    )
    birthday = models.ForeignKey(
        PersonBirthday,
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='toBurthdayFromUser'
    )
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
        null=False, blank=False,
        related_name='toEmailFromUser'
    )
    phone = models.ForeignKey(
        MobilePhone,
        on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='toPhoneFromUser'
    )
    card = models.ForeignKey(
        PersonCard,
        on_delete=models.CASCADE,
        related_name='toCardFromUser'
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
