from django.contrib import admin
from .models import KPI, Machine, Measurements
# Register your models here.

admin.site.register(Machine)
admin.site.register(Measurements)
admin.site.register(KPI)