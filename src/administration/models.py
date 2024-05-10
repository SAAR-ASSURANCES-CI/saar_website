from django.db import models

# Create your models here.


class Caroussel(models.Model):
    titre = models.CharField(max_length=150, null=True, blank=True)
    contenu = models.TextField(null=True, blank=True)
    path = models.ImageField(upload_to='img/')

    