from django.shortcuts import render
from rest_framework import generics
from.models import Paie
from rest_framework.permissions import IsAdminUser
from .serialisers import PaieSerialiser
from rest_framework_simplejwt.authentication import JWTAuthentication

class BaseMixin:
    queryset = Paie.objects.all()
    serializer_class = PaieSerialiser
    permission_classes=[IsAdminUser]
    authentication_classes=[JWTAuthentication]
    

class PaieListCreate(BaseMixin, generics.ListCreateAPIView):
    pass
   

class PaieDetailUpdateDestroy(BaseMixin, generics.RetrieveUpdateDestroyAPIView):
    pass
