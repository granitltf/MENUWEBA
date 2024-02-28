from django.db import models

# Create your models here.
class Boire(models.Model):
    nom_boisson = models.CharField(max_length=200,null=True)
    taille_boisson = models.CharField(max_length=20,null=True)
    prix_boisson = models.FloatField(null= True)


    def __str__(self):
        return self.nom_boisson