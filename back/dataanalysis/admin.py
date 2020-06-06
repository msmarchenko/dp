from django.contrib import admin
from .models import KPI, Machine, Order, User, Parameter
# Register your models here.

admin.site.register(Machine)
# admin.site.register(Measurements)
admin.site.register(KPI)
admin.site.register(User)
admin.site.register(Order) 
admin.site.register(Parameter)



admin.site.site_header = "Admin Panel DataMinig"
admin.site.site_header = 'Admin Panel DataMinig'
admin.site.index_title = 'Admin Panel DataMinig'