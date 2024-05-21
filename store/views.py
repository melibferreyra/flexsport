from django.shortcuts import render, redirect
from .models import Equipo, Liga, Categoria, Jugadores, Publicidad
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect

#vista principal donde se visualizan las ligas
def home(request):
    categorias = Categoria.objects.all()
    publicidades = Publicidad.objects.all()

    ligas_por_categoria = {}
    for categoria in categorias:
        ligas_por_categoria[categoria] = Liga.objects.filter(categoria=categoria)
    
    return render(request, 'home.html', { 'ligas_por_categoria': ligas_por_categoria, 'publicidades': publicidades })

#vista de equipos correspondientes a la liga
def equipos(request, liga_nombre):
    liga = get_object_or_404(Liga, nombre=liga_nombre)
    equipos_por_liga = Equipo.objects.filter(liga=liga)
    categoria_de_liga = liga.categoria
    equipos_por_categoria = Equipo.objects.filter(liga__categoria=categoria_de_liga)

    if not equipos_por_liga:
        equipo_nombre_lower = liga_nombre.lower()
        return HttpResponseRedirect(f"https://flexsportarg.com.ar/search/?q={equipo_nombre_lower}")
    
    return render(request, 'equipos.html', { 'equipos_por_liga': equipos_por_liga, 'liga': liga, 'equipos_por_categoria': equipos_por_categoria })


def productos_por_equipo(request, equipo_nombre):
    equipo_nombre_lower = equipo_nombre.lower()
    
    return redirect(f"https://flexsportarg.com.ar/search/?q={equipo_nombre_lower}")

def carrera_en_camisetas(request):
    jugadores = Jugadores.objects.all()
    return render(request, 'carrera-en-camisetas.html', { 'jugadores': jugadores })
    
def carrera_en_camisetas_jugador(request, jugador_nombre):
    jugador = get_object_or_404(Jugadores, nombre=jugador_nombre)
    return render(request, 'carrera-en-camisetas-jugador.html', { 'jugador': jugador })
    

    
    

    
    
# REDIRIGE AL FLEX, A LA CAMISETA DEL JUGADOR
# def productos_por_jugador(request, jugador_nombre):
#     jugador_nombre_lower = jugador_nombre.lower()
#     return redirect(f"https://flexsportarg.com.ar/search/?q={jugador_nombre_lower}")