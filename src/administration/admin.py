from django.contrib import admin
from .models import Caroussel, Actualite, Produit, Sinistre, Agence, AgentGeneral, Categorie, Temoignage, DetailProduit, Garantie, Formule


class CarouselAdmin(admin.ModelAdmin):
    list_display = ('id','titre', 'contenu', 'lien', 'created_at', 'updated_at', 'creator')
    # prepopulated_fields = {'slug': ('titre',)}

class ActualiteAdmin(admin.ModelAdmin):
    list_display = ('id','titre', 'contenu', 'date_publication',)

class CategorieAdmin(admin.ModelAdmin):
    list_display = ('id', 'libelle', 'created_at', 'updated_at', 'creator')

class ProduitAdmin(admin.ModelAdmin):
    list_display = ('id', 'slug', 'titre', 'contenu', 'categorie', 'path', 'is_visible', 'created_at', 'updated_at', 'creator')
    list_filter = ("is_visible", "categorie")

class DetailProduitAdmin(admin.ModelAdmin):
    list_display = ('id', 'produit', 'path', 'contenu', 'qui', 'pourquoi', 'comment', 'que_faire','autre', 'created_at', 'updated_at', 'creator')    

class FormuleAdmin(admin.ModelAdmin):
    list_display = ('id','libelle', 'produit', 'description','created_at', 'updated_at', 'creator')    

class GarantieAdmin(admin.ModelAdmin):
    list_display = ('id','libelle', 'produit', 'description','created_at', 'updated_at', 'creator')

class AgentGeneralAdmin(admin.ModelAdmin):
    list_display = ('id','designation', 'localite', 'contact', 'created_at', 'updated_at', 'creator')      

class TemoignageAdmin(admin.ModelAdmin):
    list_display = ('id','contenu', 'name', 'localisation', 'date_publication')

class SinistreAdmin(admin.ModelAdmin):
    list_display = ('date_sinistre', 'lieu_sinistre', 'periode_du', 'periode_au', 
            'numero_police', 
            'intervention',
            'nom_a',
            'adresse_a',
            'phone_a',
            'email_a',
            'marque_a',
            'imma_a',
            'visite_du_a',
            'visite_au_a',
            'usage_a',
            'conducteur_a',
            'adresse_conducteur_a',
            'phone_conducteur_a',
            'profession_conducteur_a',
            'numero_permis',
            'date_delivrance_a',
            'lieu_delivrance_a',
            'categorie_a',
            'dure_a',
            'constat_a',
            'salarie_a',
            'nom_b',
            'adresse_b',
            'phone_b',
            'email_b',
            'marque_b',
            'imma_b',
            'visite_du_b',
            'visite_au_b',
            'usage_b',
            'conducteur_b',
            'adresse_conducteur_b',
            'phone_conducteur_b',
            'profession_conducteur_b',
            'numero_permis_b',
            'date_delivrance_b',
            'lieu_delivrance_b',
            'categorie_b',
            'dure_b',
            'constat_b',
            'salarie_b',
            'circonstance',
            'dommages',) 

class AgenceAdmin(admin.ModelAdmin):
    list_display = ('id','titre', 'situation', 'contact', 'localisation', 'zone', 'created_at', 'updated_at', 'creator')            


# Register your models here.

# Panneau défilant
admin.site.register(Caroussel, CarouselAdmin)

# Actualités
admin.site.register(Actualite, ActualiteAdmin)

# Témoignages
admin.site.register(Temoignage, TemoignageAdmin)

# Categorie
admin.site.register(Categorie, CategorieAdmin)

# Produits
admin.site.register(Produit, ProduitAdmin)

admin.site.register(DetailProduit, DetailProduitAdmin)

admin.site.register(Formule, FormuleAdmin)

admin.site.register(Garantie, GarantieAdmin)

admin.site.register(Sinistre, SinistreAdmin)

admin.site.register(Agence, AgenceAdmin)

admin.site.register(AgentGeneral, AgentGeneralAdmin)