from database import Database

tarifas = Database("Tarifas", "gama", "tarifa")

def definirTarifas(gama, tarifa):
    return tarifas.insert(gama, tarifa)

def actualizarTarifa(gama, tarifa):
    if gama == "Baja":
        return tarifas.update(1, gama, tarifa)
    elif gama == "Media":
        return tarifas.update(2, gama, tarifa)
    else:
        return tarifas.update(3, gama, tarifa)

def traerTarifas():
    pass




