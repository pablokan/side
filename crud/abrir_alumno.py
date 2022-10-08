from database import Database

alumno = Database("Alumno", "nombre", "fecha_nac", "comision", "nota")
datos = alumno.select()
print(datos)