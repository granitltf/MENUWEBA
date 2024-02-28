from django.db import models

# Create your models here.

class Manger(models.Model):
    nom_plat = models.CharField(max_length=200, null= True)
    prix_plat = models.FloatField(null= True)

    def __str__(self):
        return self.nom_plat