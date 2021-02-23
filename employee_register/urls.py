from django.urls import path, include 
from . import views

urlpatterns = [
    path('', views.employee_form, name='employee_insert'), #solicitudes get y post para operaciones de agregar/insertar
    path('list/', views.employee_list, name='employee_list'), #solicitudes get y post para listar todos los registros
    path('delete/<int:id>/', views.employee_delete, name='employee_delete'),
    path('<int:id>/', views.employee_form, name='employee_update') #solicitudes get y post para operaciones de actualizar registros
]
