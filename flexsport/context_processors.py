from store.models import Equipo, Liga, Jugadores

def equipos_ligas(request):
    equipos = Equipo.objects.all()
    ligas = Liga.objects.all()
    jugadores = Jugadores.objects.all()
    return {'equipos': equipos, 'ligas': ligas, 'jugadores': jugadores }