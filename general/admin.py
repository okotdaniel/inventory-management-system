from django.contrib import admin

# Register your models here.
from .models import Electronics,Report,AssignElectronics

admin.site.register(Electronics)
admin.site.register(Report)
admin.site.register(AssignElectronics)
