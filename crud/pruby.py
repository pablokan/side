def foo(db, *args):
    print(args)


header = {
            "id": "id", 
            "nombre": "Nombre", 
            "fecha_nac": "Fecha de Nacimiento", 
            "comision": "Comisión", 
            "nota": "Nota"
            }

alumnos = alumnos = foo("Alumno", *list(header.keys()))
# ('id', 'nombre', 'fecha_nac', 'comision', 'nota')
