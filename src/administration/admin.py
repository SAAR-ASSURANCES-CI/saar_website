from django.contrib import admin
from .models import Caroussel, Actualite


class CarouselAdmin(admin.ModelAdmin):
    list_display = ('id','titre', 'contenu', 'created_at', 'updated_at', 'creator')
    # prepopulated_fields = {'slug': ('titre',)}


class ActualiteAdmin(admin.ModelAdmin):
    list_display = ('id','titre', 'contenu', 'date_publication',)


# Register your models here.

# Panneau défilant
admin.site.register(Caroussel, CarouselAdmin)

# Articles
admin.site.register(Actualite, ActualiteAdmin)