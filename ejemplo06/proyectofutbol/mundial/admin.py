from django.contrib import admin

# Register your models here.
from mundial.models  import Estadios,Equipos

admin.site.register(Estadios)
admin.site.register(Equipos)