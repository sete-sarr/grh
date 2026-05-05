from django.urls import path
from . import views

urlpatterns = [
    path('postes/', views.PosteListCreate.as_view(), name='poste-list'),
]                   