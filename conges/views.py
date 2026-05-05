from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Conge
from .serializers import CongeSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication


class ApiBase:
    queryset = Conge.objects.all()
    serializer_class = CongeSerializer
    authentication_classes = [JWTAuthentication]   # ✅ ICI
    permission_classes = [permissions.IsAuthenticated]  # ✅ ICI


    def get_queryset(self):
        return Conge.objects.filter(employe=self.request.user.employe)


class CongeListCreate(ApiBase, generics.ListCreateAPIView):

    def perform_create(self, serializer):
        serializer.save(employe=self.request.user.employe)


class CongeRetrieveUpdateDestroy(ApiBase, generics.RetrieveUpdateDestroyAPIView):

    def perform_update(self, serializer):
        serializer.save(employe=self.request.user.employe)




# Create your views here.
