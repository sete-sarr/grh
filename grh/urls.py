
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path('api/', include('employes.urls')),
    path('api/', include('departements.urls')),
    path('api/', include('paies.urls')),
    path('api/', include('conges.urls')),
    path('api/', include('presences.urls')),
    path('api/', include('accounts.urls')),
    path('api/', include('postes.urls')),
]
