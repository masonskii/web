from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, username, password, **extra_fields):
        """
        Create and save a user with the given username, email,
        full_name, and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        if not username:
            raise ValueError('The given username must be set')
        # email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(
            email=email, username=username,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(
            email, username, password, **extra_fields
        )

    def create_superuser(self, email, username, full_name, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(
            email, username, full_name, password, **extra_fields
        )


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


class Person(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    person_id = models.AutoField(primary_key=True)
    username = models.ForeignKey(
        PersonLogin,
        on_delete=models.CASCADE,
        null=False, blank=False,
        related_name='toLoginFromUser'
    )
    bio = models.CharField(
        max_length=160,
        null=True,
        blank=True
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
        default=10,
        on_delete=models.CASCADE,
        null=False, blank=False,
        unique=True,
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
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_organizate = models.BooleanField(default=False)
    organization_name = models.CharField(max_length=99, null=True, blank=True)
    type_activity = models.CharField(max_length=99, null=True, blank=True)

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username', 'bio', 'role']

    objects = UserManager()

    def get_full_name(self):
        return self.name.name, self.surname.surname, self.ndName.ndName

    def __str__(self):
        return self.email

    def get_short_name(self):
        return self.email

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)


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
