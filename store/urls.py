from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('equipos/<str:liga_nombre>/', views.equipos, name='equipos'),
    path('productos/<str:equipo_nombre>/', views.productos_por_equipo, name='productos_por_equipo'),
    path('carrera-en-camisetas/', views.carrera_en_camisetas, name='carrera_en_camisetas'),
    # url para jugador especifico
    path('carrera-en-camisetas/<str:jugador_nombre>/', views.carrera_en_camisetas_jugador, name='carrera_en_camisetas_jugador'),
]
