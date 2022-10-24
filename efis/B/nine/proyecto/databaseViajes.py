from database import Database

viajes = Database("Viajes", "chofer", "distancia", "ganancia")

def agregarViaje(nombre, distancia, ganancia):
    return viajes.insert(nombre, distancia, ganancia)
