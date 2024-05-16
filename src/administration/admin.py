from django.contrib import admin
from .models import Caroussel, Actualite, Produit


class CarouselAdmin(admin.ModelAdmin):
    list_display = ('id','titre', 'contenu', 'created_at', 'updated_at', 'creator')
    # prepopulated_fields = {'slug': ('titre',)}

class ActualiteAdmin(admin.ModelAdmin):
    list_display = ('id','titre', 'contenu', 'date_publication',)


class ProduitAdmin(admin.ModelAdmin):
    list_display = ('id','titre', 'contenu', 'created_at', 'updated_at', 'creator')    


# Register your models here.

# Panneau défilant
admin.site.register(Caroussel, CarouselAdmin)

# Actualités
admin.site.register(Actualite, ActualiteAdmin)

# Produits
admin.site.register(Produit, ProduitAdmin)