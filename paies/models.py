from django.db import models
from django.db import models
from employes.models import Employe

class Paie(models.Model):
    employe = models.ForeignKey(Employe, on_delete=models.CASCADE)
    mois = models.DateField()

    salaire_base = models.DecimalField(max_digits=10, decimal_places=2)
    prime = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    retenue = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    class Meta:
        indexes =[models.Index(fields=['employe', 'mois', 'salaire_base'])]
        verbose_name='employe'

    def salaire_total(self):
        return self.salaire_base + self.prime - self.retenue
    

    def __str__(self):
        return f"{self.employe} - {self.mois}"

# Create your models here.
