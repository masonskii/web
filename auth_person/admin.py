from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Person)
admin.site.register(Role)
admin.site.register(Logo)
admin.site.register(Department)
admin.site.register(Specialization)
admin.site.register(PersonSpecs)
admin.site.register(Membership)
admin.site.register(Email)
admin.site.register(MobilePhone)