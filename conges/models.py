from django.db import models
from employes.models import Employe

class Conge(models.Model):
    STATUT_CHOIX = (
        ('en_attente', 'En attente'),
        ('approuve', 'Approuvé'),
        ('refuse', 'Refusé'),
    )

    employe = models.ForeignKey(Employe, on_delete=models.CASCADE)
    date_debut = models.DateField()
    date_fin = models.DateField()
    motif = models.TextField()

    statut = models.CharField(max_length=20, choices=STATUT_CHOIX, default='en_attente')

    def __str__(self):
        return f"{self.employe} - {self.statut}"

# Create your models here.
