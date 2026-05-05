from django.contrib import admin
from django.contrib import admin
from .models import Paie

@admin.register(Paie)
class PaieAdmin(admin.ModelAdmin):
    list_display = ('employe', 'mois', 'salaire_base', 'prime', 'retenue')
    list_filter = ('employe', 'mois')
    search_fields = ('employe__nom', 'employe__prenom')

# Register your models here.
