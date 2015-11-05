from django.contrib import admin

# Register your models here.
from .models import County, Lake, Report

admin.site.register(County)
admin.site.register(Lake)
admin.site.register(Report)