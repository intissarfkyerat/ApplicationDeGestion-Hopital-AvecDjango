from django.contrib import admin
from .models import Patient,Doctor,Appoinment
# Register your models here.
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Appoinment)
