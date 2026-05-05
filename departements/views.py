from django.shortcuts import render
from rest_framework import generics

from rest_framework.permissions import IsAuthenticated
from .serializers import EmployeSerializer , DepartementSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Departement

class DepartementList(generics.ListCreateAPIView):
    queryset = Departement.objects.all()
    serializer_class = DepartementSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

# Create your views here.
