from django.db import models
from django.conf import settings
from departements.models import Departement
from postes.models import Poste

 
class Employe(models.Model):
    """Modèle représentant un employé de l'organisation."""

    utilisateur = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='employe',
        help_text="Utilisateur associé à cet employé"
    )
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telephone = models.CharField(max_length=20)
    adresse = models.TextField()
 
    departement = models.ForeignKey(
        Departement,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='employes'
    )
    poste = models.ForeignKey(
        Poste,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='employes'
    )
 
    date_embauche = models.DateField()
    salaire = models.DecimalField(max_digits=10, decimal_places=2)
    date_creation = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    date_modification = models.DateTimeField(auto_now=True , null=True, blank=True)
 
    def __str__(self):
        return f"{self.prenom} {self.nom}"
 
    class Meta:
        ordering = ['nom', 'prenom']
        verbose_name = "Employé"
        verbose_name_plural = "Employés"
        indexes = [
            models.Index(fields=['nom', 'prenom']),
            models.Index(fields=['email']),
        ]
 