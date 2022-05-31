from django.db import models


# Create your models here.
class OrgPullRequest(models.Model):
    person_email = models.EmailField(default=None)
    person_telephone = models.CharField(max_length=99, default=None)
    name_org = models.CharField(max_length=99)
    logo_org = models.ImageField(upload_to='files/image/org_logo_request/%Y-%m-%d/')
    address = models.CharField(max_length=199, null=False, blank=False)
    type_org = models.CharField(max_length=99)
    description = models.CharField(max_length=999)
    is_pull = models.BooleanField(default=False)
    date_created_request = models.DateField(auto_now=True)


class PersonPullRequest(models.Model):
    name = models.CharField(max_length=99)
    role = models.CharField(max_length=99)
    description = models.CharField(max_length=999)
    date_created_request = models.DateField(auto_now=True)


"""    role = (
        ('creater', u'Creater'),
        ('moderator', u'Moderator'),
        ('org', u'Organizate'),
        ('admin', u'Admin')
    )"""
