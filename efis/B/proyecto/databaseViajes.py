from database import Database

viajes = Database("Viajes", "chofer", "distancia", "ganancia")

def agregarViaje(nombre, distancia, ganancia):
    return viajes.insert(nombre, distancia, ganancia)

def traerGanancia():
    data = viajes.select()
    datos = list()
    for i in range(len(data)):
        datos.append(data[i][3])
    return datos
