from django.urls import path

from AppCoder import views





urlpatterns = [
   
    path('', views.inicio, name="Inicio"), #esta era nuestra primer view

    path('pacientes', views.pacientes, name="Pacientes"),
    path('medicos', views.medicos, name="Medicos"),
    path('practicas', views.practicas, name="Practicas"),

    path('buscar/', views.buscar),
   
]

