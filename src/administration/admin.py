from django.contrib import admin
from .models import Caroussel, Actualite

# Register your models here.

# Panneau défilant
admin.site.register(Caroussel)
admin.site.register(Actualite)