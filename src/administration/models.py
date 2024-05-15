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

    #slug = models.SlugField(max_length=200, unique=True, default="")

    def __str__(self):
        return self.path.url

    
    # def get_absolute_url(self):
    #     return reverse('carousel_detail', kwargs={'slug': self.slug})
    
    # def save(self, *args, **kwargs):
    #     value = self.titre
    #     self.slug = slugify(value, allow_unicode=True)
    #     return super().save(*args, **kwargs)
    


# ACTUALITES
class Actualite(models.Model):
    titre = models.CharField(max_length=150, blank=True, default="")
    contenu = models.TextField(blank=True, default="")
    date_publication = models.DateField()
    path = models.ImageField(upload_to='img/')

    def __str__(self):
        return self.path.url
    


 # ACTUALITES
class Produit(models.Model):
    titre = models.CharField(max_length=100)
    contenu = models.TextField(blank=True, default="")
    path = models.ImageField(upload_to='img/')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(blank=True, null=True)

    creator = models.CharField(max_length=100, blank=True)

    #slug = models.SlugField(max_length=200, unique=True, default="")

    def __str__(self):
        return self.path.url

    