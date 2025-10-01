from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from administration.models import Produit  # Adaptez selon votre modèle

class StaticViewSitemap(Sitemap):
    """Sitemap pour les pages statiques"""
    priority = 1.0
    changefreq = 'weekly'
    protocol = 'https'

    def items(self):
        # Vos pages principales
        return [
            'index',           # Page d'accueil
            'about',           # À propos
            'about_grp',       # À propos du groupe
            'contact',         # Contact
            'agences',         # Nos agences
            'valeurs'          # Nos valeurs
        ]
    
    def location(self, item):
        return reverse(item)
    
    def priority_func(self, item):
        # Priorité personnalisée selon la page
        priorities = {
            'index': 1.0,
            'contact': 0.9,
            'about': 0.8,
            'agences': 0.8,
            'about_grp': 0.7,
            'valeurs': 0.7,
            'reclamation': 0.6,
        }
        return priorities.get(item, 0.5)


class ProduitSitemap(Sitemap):
    """Sitemap pour les produits d'assurance"""
    changefreq = "weekly"
    priority = 0.8
    protocol = 'https'

    def items(self):
        # Retourne tous les produits visibles
        return Produit.objects.filter(est_visible=True)
    
    def lastmod(self, obj):
        # Date de dernière modification
        return obj.date_modification if hasattr(obj, 'date_modification') else None
    
    def location(self, obj):
        # URL du produit
        return reverse('produit_detail', kwargs={'slug': obj.slug})


# Dictionnaire de tous vos sitemaps
sitemaps = {
    'static': StaticViewSitemap,
    'produits': ProduitSitemap,
}