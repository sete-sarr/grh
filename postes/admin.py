from django.contrib import admin
from django.contrib import admin
from .models import Poste

@admin.register(Poste)
class PosteAdmin(admin.ModelAdmin):
    list_display = ('intitule',)
    search_fields = ('intitule',)
# Register your models here.
