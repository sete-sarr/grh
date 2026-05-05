from django.urls import path
from .views import CongeListCreate

urlpatterns=[
    path('conges/', CongeListCreate.as_view(), name='conge-list-create'),
]