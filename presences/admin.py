from django.contrib import admin
from django.contrib import admin
from .models import Presence

@admin.register(Presence)
class PresenceAdmin(admin.ModelAdmin):
    list_display = ('employe', 'date', 'heure_arrivee', 'heure_depart')

# Register your models here.
