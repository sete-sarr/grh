from rest_framework import serializers
from .models import Paie
from employes.models import Employe
class EmployeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employe
        fields = '__all__'


class PaieSerialiser(serializers.ModelSerializer):
    employe = EmployeSerializer(read_only=True)
    class Meta:
        model = Paie
        fields = '__all__'