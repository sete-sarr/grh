from django.db import models
from django.db import models
from employes.models import Employe

class Presence(models.Model):
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE)
    date = models.DateField()

    heure_arrivee = models.TimeField()
    heure_depart = models.TimeField()

    def __str__(self):
        return f"{self.employe} - {self.date}"
# Create your models here.
