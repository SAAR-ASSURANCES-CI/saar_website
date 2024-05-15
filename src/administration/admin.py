from django.contrib import admin
from .models import Caroussel, Actualite, Produit


class CarouselAdmin(admin.ModelAdmin):
    list_display = ('id','titre', 'contenu', 'created_at', 'updated_at', 'creator')
    # prepopulated_fields = {'slug': ('titre',)}


class ProduitAdmin(admin.ModelAdmin):
    list_display = ('id','titre', 'contenu', 'created_at', 'updated_at', 'creator')    


class ActualiteAdmin(admin.ModelAdmin):
    list_display = ('id','titre', 'contenu', 'date_publication',)


# Register your models here.

# Panneau défilant
admin.site.register(Caroussel, CarouselAdmin)

# Produits
admin.site.register(Produit, ProduitAdmin)

# Actualités
admin.site.register(Actualite, ActualiteAdmin)