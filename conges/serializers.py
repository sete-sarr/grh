from rest_framework import serializers
from .models import Conge
from employes.models import Employe
class EmplyeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employe
        fields = ['id', 'nom', 'prenom', 'email']
class CongeSerializer(serializers.ModelSerializer):
    employe = EmplyeSerializer(read_only=True)
    class Meta:
        model = Conge
        fields = ['id', 'date_debut', 'date_fin', 'motif', 'employe']

