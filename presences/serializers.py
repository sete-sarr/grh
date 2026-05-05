from rest_framework import serializers
from .models import Presence
from employes.models import Employe
class EmployeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employe
        fields = '__all__'

class PresenceSerializer(serializers.ModelSerializer):
    employe = EmployeSerializer(read_only=True)

    class Meta:
        model = Presence
        fields = '__all__'