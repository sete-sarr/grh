from django.contrib import admin
from django.contrib import admin
from .models import Conge

@admin.register(Conge)
class CongeAdmin(admin.ModelAdmin):
    list_display = ('employe', 'date_debut', 'date_fin', 'statut', 'motif')
    list_filter = ('statut',)

# Register your models here.
