import datetime
from datetime import timezone

from django.contrib.humanize.templatetags.humanize import naturaltime
from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.base_user import BaseUserManager
from django.http import HttpResponse

now = datetime.datetime.now(timezone.utc)


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
    """
    Model table Role in project db

    Example:
    SET:
        var = Role()
        var.role = object
        var.save()
    ----------------------------
    GET:
        var = Role.objects.get(id = object )
    """
    role_id = models.AutoField(primary_key=True)
    role = models.CharField(max_length=20)


class PersonCard(models.Model):
    """
    Model table PersonCard in project db
        Example:
    SET:
        var = PersonCard()
        var.number = object
        var.secret_code = object
        var.save()
    ----------------------------
    GET:
        var = PersonCard.objects.get(id = object)
    """
    card_id = models.AutoField(primary_key=True)
    number = models.CharField(max_length=12, unique=True)
    secret_code = models.CharField(max_length=3)


class Organization(models.Model):
    name = models.CharField(max_length=99, null=False, blank=False)
    type = models.CharField(max_length=99, null=False, blank=False)
    description = models.CharField(max_length=999, null=False, blank=False)
    logo = models.ImageField(upload_to='files/image/org_logo/%Y-%m-%d/', null=True, blank=True)
    address_org = models.CharField(max_length=199, null=False, blank=False)


class Person(AbstractBaseUser, PermissionsMixin):
    """
    Model table Person in project db, central table on project
        Example:
    SET:
        var = Person(request.POST)
        var.save()
    ----------------------------
    GET:
        var = Person.objects.get(id = object)
    """
    sex_choice = (
        (0, 'Male'),
        (1, 'Female')
    )
    username_validator = UnicodeUsernameValidator()

    person_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=99, null=False, blank=False)
    bio = models.CharField(
        max_length=160,
        null=True,
        blank=True
    )
    name = models.CharField(
        max_length=99,
        null=True,
        blank=True
    )
    sex = models.CharField(max_length=1, choices=sex_choice)
    skills = models.CharField(max_length=999, null=True, blank=True)
    surname = models.CharField(
        max_length=99,
        null=True,
        blank=True
    )
    ndName = models.CharField(
        max_length=99,
        null=True,
        blank=True
    )
    birthday = models.DateField(
        null=True,
        blank=True
    )
    role = models.ForeignKey(
        Role,
        on_delete=models.CASCADE,

    )
    logo = models.ImageField(upload_to='files/image/user_logo/%Y-%m-%d/', null=True, blank=True)
    email = models.EmailField(max_length=50, null=False, blank=False, unique=True)
    phone = models.CharField(
        max_length=12,
        null=True, blank=True,
    )
    card = models.ForeignKey(
        PersonCard,
        on_delete=models.CASCADE,
        related_name='toCardFromUser'
    )
    specialization = models.CharField(max_length=999)
    balance = models.DecimalField(max_digits=19, decimal_places=10)
    registrationDate = models.DateTimeField(auto_now=True)
    lastEntrance = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_organizate = models.BooleanField(default=False)
    last_online = models.DateTimeField(blank=True, null=True)
    organizated = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        default=0
    )
    country = models.CharField(max_length=99)
    address = models.CharField(max_length=999)
    translate = models.IntegerField(default=0)
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username', 'password']

    objects = UserManager()

    def get_full_name(self):
        return self.name, self.surname, self.ndName

    def __str__(self):
        return self.email

    def get_short_name(self):
        return self.email

    def sell(self, summary):
        try:
            if not self.check_balance():
                return False
            if self.balance < summary:
                return False
            if type(summary) is not int():
                return False
            return True
        except Exception:
            raise Exception
    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def check_balance(self):
        return self.balance == 0

    # In this method, check that the date of the last visit is not older than 15 minutes
    def is_online(self):
        if self.last_online:
            return (datetime.datetime.now(timezone.utc) - self.last_online) < datetime.timedelta(minutes=15)
        return False

    # If the user visited the site no more than 15 minutes ago,
    def get_online_info(self):
        if self.is_online():
            # then we return information that he is online
            return 'Online'
        if self.last_online:
            # otherwise we write a message about the last visit
            return ('Last visit {}').format(naturaltime(self.last_online))
            # If you have only recently added information about a user visiting the site
            # then for some users there may not be any information about the visit, we will return information that the last visit is unknown
        return 'Unknown'


class Comm(models.Model):
    sender = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name='senderComm'
    )
    recipient = models.ForeignKey(
        Person,
        on_delete=models.CASCADE,
        related_name='recipientComm'
    )
    description = models.CharField(max_length=999)
    date_created = models.DateTimeField(auto_now=True)


class Department(models.Model):
    """
     Model table Department in project db
         Example:
     SET:
         var = Department(request.POST)
         var.save()
     ----------------------------
     GET:
         var = Department.objects.get(id = object)
     """
    departmen_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, null=False)


class Membership(models.Model):
    """
     Model table Membership in project db
         Example:
     SET:
         var = Membership(request.POST)
         var.save()
     ----------------------------
     GET:
         var = Membership.objects.get(id = object)
     """
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
