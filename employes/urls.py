from django.urls import path
from .views import EmployeList, EmployeCreate, EmployeUpdate, EmployeDetail, EmployeDelete

urlpatterns = [
    path('employes/', EmployeList.as_view(), name='employe-list'),
    path('employes/create/', EmployeCreate.as_view(), name='employe-create'),
    path('employes/<int:pk>/', EmployeDetail.as_view(), name='employe-detail'),
    path('employes/update/<int:pk>/', EmployeUpdate.as_view(), name='update'),
    path('employes/delete/<int:pk>/',EmployeDelete.as_view() )

]