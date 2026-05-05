from django.shortcuts import render
from rest_framework import generics

from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import PosteSerializer
from .models import Poste
from rest_framework_simplejwt.authentication import JWTAuthentication
class PosteListCreate(generics.ListCreateAPIView):
    queryset = Poste.objects.all()
    serializer_class = PosteSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]

# Create your views here.
