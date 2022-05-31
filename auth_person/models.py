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
    balance = models.DecimalField(max_digits=19, decimal_places=10)
    registrationDate = models.DateTimeField(auto_now=True)
    lastEntrance = models.DateTimeField(auto_now=True)
    is_staff = models.BooleanField(default=False)
    is_organizate = models.BooleanField(default=False)
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

    def email_user(self, subject, message, from_email=None, **kwargs):
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def check_balance(self):
        return self.balance == 0


class Organization(models.Model):
    name = models.CharField(max_length=99, null=False, blank=False)
    type = models.CharField(max_length=99, null=False, blank=False)
    description = models.CharField(max_length=999, null=False, blank=False)
    logo = models.ImageField(upload_to='files/image/org_logo/%Y-%m-%d/', null=True, blank=True)
    address = models.CharField(max_length=199, null=False, blank=False)
    user = models.ForeignKey(Person, on_delete=models.CASCADE)


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


class Specialization(models.Model):
    """
     Model table Specialization in project db
         Example:
     SET:
         var = Specialization(request.POST)
         var.save()
     ----------------------------
     GET:
         var = Specialization.objects.get(id = object)
     """
    specialization_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20, null=False)


class PersonSpecs(models.Model):
    """
     Model table PersonSpecs in project db
         Example:
     SET:
         var = PersonSpecs(request.POST)
         var.save()
     ----------------------------
     GET:
         var = PersonSpecs.objects.get(id = object)
     """
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
