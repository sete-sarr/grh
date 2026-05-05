from django.shortcuts import render
from rest_framework import generics
from .models import Presence
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import PresenceSerializer

class PresenceListCreate(generics.ListCreateAPIView):
    queryset = Presence.objects.all()
    serializer_class = PresenceSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['employe__nom', 'employe__prenom', 'date']

class PresenceRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Presence.objects.all()
    serializer_class = PresenceSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]   
# Create your views here.

# views.py
from rest_framework.views import APIView
from rest_framework.response import Response

from django.utils import timezone


class PointerView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user

        # Vérifier si déjà pointé aujourd’hui
        today = timezone.now().date()

        if Presence.objects.filter(employe=user, date=today).exists():
            return Response({"error": "Déjà pointé aujourd’hui"}, status=400)

        Presence.objects.create(
            employe=user,
            date=today,
            heure_arrivee=timezone.now().time()
        )

        return Response({"message": "Pointage enregistré"})
