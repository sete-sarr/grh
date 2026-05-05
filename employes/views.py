from django.shortcuts import render
from rest_framework import generics
from .models import Employe
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import EmployeSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication

class EmployeList(generics.ListCreateAPIView):
    queryset = Employe.objects.all()
    serializer_class = EmployeSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminUser]
    
    

# Create your views here.
class EmployeCreate(generics.CreateAPIView):
    queryset = Employe.objects.all()
    serializer_class = EmployeSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(utilisateur=self.request.user)
class EmployeDetail(generics.RetrieveAPIView):
    queryset = Employe.objects.all()
    serializer_class = EmployeSerializer
    permission_classes = [IsAuthenticated] 
class EmployeUpdate(generics.UpdateAPIView):
    queryset = Employe.objects.all()
    serializer_class = EmployeSerializer
    permission_classes = [IsAuthenticated]
    def perform_update(self, serializer):  
        serializer.save(utilisateur=self.request.user)
class EmployeDelete(generics.DestroyAPIView):
    queryset = Employe.objects.all()
    serializer_class = EmployeSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]


