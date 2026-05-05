from django.contrib import admin
from django.contrib import admin
from .models import Employe

@admin.register(Employe)
class EmployeAdmin(admin.ModelAdmin):
    list_display = ('nom', 'prenom', 'email', 'departement', 'poste', 'date_embauche')
    search_fields = ('nom', 'prenom', 'email')
    list_filter = ('departement', 'poste')

# Register your models here.
