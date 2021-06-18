from django.contrib import admin
from .models import *

admin.site.register(Person)
admin.site.register(Medic)
admin.site.register(Vaccine)
admin.site.register(Place)
admin.site.register(PlaceHasVaccines)
admin.site.register(Appointment)
