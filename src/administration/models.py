from django.db import models

# from django.utils.text import slugify

# Create your models here.

# PANNEAU DEFILANT
class Caroussel(models.Model):
    titre = models.CharField(max_length=150, blank=True, default="")
    contenu = models.TextField(blank=True, default="")
    path = models.ImageField(upload_to='img/')

    def __str__(self):
        return self.path.url
    


# ACTUALITES
class Actualite(models.Model):
    titre = models.CharField(max_length=150, blank=True, default="")
    contenu = models.TextField(blank=True, default="")
    date_publication = models.DateField()
    path = models.ImageField(upload_to='img/')

    def __str__(self):
        return self.path.url

    