from django.contrib import admin

from appointmentapp.models import appointment

from .models import *

# Register your models here.
admin.site.register(User)
class appointmentStacked(admin.StackedInline):
    model = appointment
    extra = 0

class doctorperso(admin.ModelAdmin):
    inlines = [appointmentStacked,]
admin.site.register(Doctor, doctorperso)
admin.site.register(Patient)
admin.site.register(Speciality)