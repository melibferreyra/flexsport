from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('equipos/<str:liga_nombre>/', views.equipos, name='equipos'),
    path('productos/<str:equipo_nombre>/', views.productos_por_equipo, name='productos_por_equipo'),
    path('productos/<str:jugador_nombre>/', views.productos_por_jugador, name='productos_por_jugador')
]
