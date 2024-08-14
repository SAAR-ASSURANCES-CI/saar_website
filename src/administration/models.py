from datetime import datetime
from typing import Iterable
from django.db import models

from django.utils.text import slugify

from django.urls import reverse

from django.utils.timezone import now


# Create your models here.

# PANNEAU DEFILANT
class Caroussel(models.Model):
    titre = models.CharField(max_length=100)
    contenu = models.TextField(blank=True, default="")
    path = models.ImageField(upload_to='img/')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    creator = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.path.url

################################################################################
    #slug = models.SlugField(max_length=200, unique=True, default="")
    
    # def get_absolute_url(self):
    #     return reverse('carousel_detail', kwargs={'slug': self.slug})
    
    # def save(self, *args, **kwargs):
    #     value = self.titre
    #     self.slug = slugify(value, allow_unicode=True)
    #     return super().save(*args, **kwargs)
    
################################################################################

# ACTUALITES
class Actualite(models.Model):
    titre = models.CharField(max_length=150, blank=True, default="")
    contenu = models.TextField(blank=True, default="")
    date_publication = models.DateField()
    path = models.ImageField(upload_to='img/')

    def __str__(self):
        return self.path.url
    


#  # PRODUITS
class Produit(models.Model):
    titre = models.CharField(max_length=100)
    contenu = models.TextField(blank=True, default="")
    path = models.ImageField(upload_to='img/')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    creator = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.path.url
    


class Sinistre(models.Model):

    date_sinistre = models.DateTimeField(verbose_name="Date et heure du sinistre")
    lieu_sinistre = models.CharField(max_length=255, verbose_name="Lieu exact du sinistre")
    periode_du = models.DateField(verbose_name="Période garantie accordée du")
    periode_au = models.DateField(verbose_name="Période garantie accordée au")
    numero_police = models.BigIntegerField(verbose_name="Numéro de police concerné")
    
    INTERVENTION_CHOICES = [
        ('Oui', 'Oui'),
        ('Non', 'Non'),
    ]
    intervention = models.CharField(
        max_length=3, 
        choices=INTERVENTION_CHOICES, 
        verbose_name="Y'a t-il eu intervention de la police ou de la gendarmerie ?"
    )

     # Informations sur l'assuré
    nom_a = models.CharField(max_length=255, verbose_name="Nom et Prénoms Assuré")
    adresse_a = models.CharField(max_length=255, verbose_name="Adresse Assuré", blank=True, null=True)
    phone_a = models.CharField(max_length=20, verbose_name="Téléphone Assuré")
    email_a = models.EmailField(verbose_name="Email", blank=True, null=True)

    # Informations sur le véhicule
    marque_a = models.CharField(max_length=100, verbose_name="Marque du véhicule Assuré")
    imma_a = models.CharField(max_length=100, verbose_name="Immatriculation Assuré")
    visite_du_a = models.DateField(verbose_name="Visite technique du")
    visite_au_a = models.DateField(verbose_name="Visite technique au")
    usage_a = models.CharField(max_length=100, verbose_name="Usage Assuré")

    # Informations sur le conducteur
    conducteur_a = models.CharField(max_length=255, verbose_name="Nom et Prénoms Conducteur")
    adresse_conducteur_a = models.CharField(max_length=255, verbose_name="Adresse Conducteur", blank=True, null=True)
    phone_conducteur_a = models.CharField(max_length=20, verbose_name="Téléphone Conducteur", blank=True, null=True)
    profession_conducteur_a = models.CharField(max_length=100, verbose_name="Profession Conducteur", blank=True, null=True)
    numero_permis = models.CharField(max_length=50, verbose_name="Numéro de permis Conducteur")
    date_delivrance_a = models.DateField(verbose_name="Date de délivrance Conducteur")
    lieu_delivrance_a = models.CharField(max_length=100, verbose_name="Lieu de délivrance Conducteur")

    CATEGORIE_CHOICES = [
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('F', 'F'),
        ('ABCDE', 'ABCDE'),
        ('BCDE', 'BCDE'),
        ('BDE', 'BDE'),
    ]
    categorie_a = models.CharField(
        max_length=6,
        choices=CATEGORIE_CHOICES,
        verbose_name="Catégorie du permis  Conducteur"
    )
    dure_a = models.PositiveIntegerField(verbose_name="Durée de validité (en année)  Conducteur")

    CONSTAT_CHOICES = [
        ('Oui', 'Oui'),
        ('Non', 'Non'),
    ]
    constat_a = models.CharField(
        max_length=3, 
        choices=CONSTAT_CHOICES, 
        verbose_name="Constat Amiable ?"
    )

    SALARIE_CHOICES = [
        ('Oui', 'Oui'),
        ('Non', 'Non'),
    ]
    salarie_a = models.CharField(
        max_length=3,
        choices=SALARIE_CHOICES,
        verbose_name="Est-il salarié de l'assuré ?"
    )

     # Informations sur la partie adverse
    nom_b = models.CharField(max_length=255, verbose_name="Nom et Prénoms de l'adversaire", blank=True, null=True)
    adresse_b = models.CharField(max_length=255, verbose_name="Adresse de l'adversaire", blank=True, null=True)
    phone_b = models.CharField(max_length=20, verbose_name="Téléphone de l'adversaire", blank=True, null=True)
    email_b = models.EmailField(verbose_name="Email de l'adversaire", blank=True, null=True)

    # Informations sur le véhicule de la partie adverse
    marque_b = models.CharField(max_length=100, verbose_name="Marque du véhicule de l'adversaire", blank=True, null=True)
    imma_b = models.CharField(max_length=100, verbose_name="Immatriculation du véhicule de l'adversaire", blank=True, null=True)
    visite_du_b = models.DateField(verbose_name="Visite technique du véhicule de l'adversaire du", blank=True, null=True)
    visite_au_b = models.DateField(verbose_name="Visite technique du véhicule de l'adversaire au", blank=True, null=True)
    usage_b = models.CharField(max_length=100, verbose_name="Usage du véhicule de l'adversaire", blank=True, null=True)

    # Informations sur le conducteur de la partie adverse
    conducteur_b = models.CharField(max_length=255, verbose_name="Nom et Prénoms du conducteur de l'adversaire", blank=True, null=True)
    adresse_conducteur_b = models.CharField(max_length=255, verbose_name="Adresse du conducteur de l'adversaire", blank=True, null=True)
    phone_conducteur_b = models.CharField(max_length=20, verbose_name="Téléphone du conducteur de l'adversaire", blank=True, null=True)
    profession_conducteur_b = models.CharField(max_length=100, verbose_name="Profession du conducteur de l'adversaire", blank=True, null=True)
    numero_permis_b = models.CharField(max_length=50, verbose_name="Numéro de permis du conducteur de l'adversaire", blank=True, null=True)
    date_delivrance_b = models.DateField(verbose_name="Date de délivrance du permis du conducteur de l'adversaire", blank=True, null=True)
    lieu_delivrance_b = models.CharField(max_length=100, verbose_name="Lieu de délivrance du permis du conducteur de l'adversaire", blank=True, null=True)

    categorie_b = models.CharField(
        max_length=6,
        choices=CATEGORIE_CHOICES,
        verbose_name="Catégorie du permis du conducteur de l'adversaire",
        blank=True, null=True
    )
    dure_b = models.PositiveIntegerField(verbose_name="Durée de validité du permis du conducteur de l'adversaire (en année)", blank=True, null=True)

    constat_b = models.CharField(
        max_length=3, 
        choices=CONSTAT_CHOICES, 
        verbose_name="Constat Amiable pour l'adversaire ?"
    )

    salarie_b = models.CharField(
        max_length=3,
        choices=SALARIE_CHOICES,
        verbose_name="Le conducteur de l'adversaire est-il salarié ?"
    )

    
     # Circonstances détaillées de l'accident
    circonstance = models.TextField(verbose_name="Circonstances", help_text="Détails du lieu de l'accident, directions suivies par les véhicules, ordre des chocs et les points de chocs sur les véhicules, etc.")
    
    # Dommages
    dommages = models.TextField(verbose_name="Dommages", help_text="Détails sur les dommages matériels et corporels. Pour les Dommages matériels, veuillez préciser le type de choc (choc lattérale droit, lattérale gauche, avant gauche, avant droit, ...), les matériels endommagés (Pare-brise, feu, ...). Pour les Dommages Corporels, veuillez préciser le nombre de blessés, le nombre de décès, l'intensité des blessures (léger, très léger, grave, très grave), le statut et l'âge des personnes concernées.")
    


    def __str__(self):
        return f"Sinistre du {self.date_sinistre} - {self.lieu_sinistre}"

    



    