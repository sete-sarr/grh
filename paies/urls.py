from django.urls import path
from .views import PaieListCreate, PaieDetailUpdateDestroy

urlpatterns = [
    path('paies/', PaieListCreate.as_view(), name='paie-list-create'),
    path('paies/<int:pk>/', PaieDetailUpdateDestroy.as_view(), name='paie-detail-update-destroy'),
]