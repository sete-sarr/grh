from rest_framework import serializers  
from .models import Departement
from employes.models import Employe

class EmployeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employe
        fields = '__all__'
class DepartementSerializer(serializers.ModelSerializer):
    # employes = serializers.PrimaryKeyRelatedField(many=True, queryset=Employe.objects.all())
    class Meta:
        model = Departement
        fields = '__all__'