from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Person)
admin.site.register(Role)
admin.site.register(Department)
admin.site.register(Membership)