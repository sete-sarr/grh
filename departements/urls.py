from django.urls import path
from .views import DepartementList

urlpatterns = [
    path('departements/', DepartementList.as_view(), name='departement-list')
    ,]  