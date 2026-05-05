from django.urls import path
from .views import PresenceListCreate, PresenceRetrieveUpdateDestroy, PointerView

urlpatterns = [
    path('presences/', PresenceListCreate.as_view(), name='presence-list-create'),  
    path('presences/<int:pk>/', PresenceRetrieveUpdateDestroy.as_view(), name='presence-retrieve-update-destroy'),
    path('pointer/', PointerView.as_view(), name='pointer'),
]   