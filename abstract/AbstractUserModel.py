from django.db import models


class Translate(models.Model):
    use_in_migrations = True

    translate = models.IntegerField()


class AddingSecondInformation:
    """
    Class on adding information on user
    """
    def __init__(self, request):
        if not request:
            raise ValueError('request is {0}. Incorrect data'.format(request))


