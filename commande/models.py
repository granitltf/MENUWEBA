from django.db import models
from mangerapp.models import Manger
from boireapp.models import Boire


class Commande(models.Model):
    manger = models.ForeignKey(Manger, on_delete=models.SET_NULL, null=True)
    boire = models.ForeignKey(Boire, on_delete=models.SET_NULL, null=True)
    #boire = models.ManyToManyField(Boire)


