from django.contrib import admin
from .models import Car, Cleaning, Upgrade
# Register your models here.
admin.site.register(Car)
admin.site.register(Cleaning)
admin.site.register(Upgrade)