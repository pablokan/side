import os
import sqlite3
from pprint import pprint


class Database:
    def __init__(self, base, *args) -> None:
        """ 
            Parámetros: Nombre de la base de datos y de los atributos 
            Ejemplo: base = Database("Persona", "nombre", "edad")
        """
        self.base = base
        self.fields = args
        conn = self.connection()
        self.sArgs = ",".join(args)
        fieldNames = f"('id' integer primary key autoincrement, {self.sArgs})"
        try:
            conn.execute(f"create table {base} {fieldNames}")
            print(f"\n{base} creada")                        
        except sqlite3.OperationalError:
            print(f"\n{base} OK")
        conn.close()

    def connection(self):
        return sqlite3.connect(f"{self.base}.db")

    def insert(self, *args):
        conn = self.connection()
        sql = f"INSERT INTO {self.base}({self.sArgs}) VALUES {args}"
        conn.execute(sql)
        print(f"\n{args} fila agregada")
        conn.commit()
        conn.close()

    def select(self) -> list:
        conn = self.connection()
        recordSet = list(conn.execute(f"SELECT * FROM {self.base}"))
        print(f"\nObtengo todas las filas de {self.base}\n")
        conn.close()
        return recordSet
        
    def delete(self, id):
        conn = self.connection()
        sql = f"DELETE FROM {self.base} WHERE id={id}"
        conn.execute(sql)
        print(f"\nFila #{id} borrada")
        conn.commit()
        conn.close()

    def update(self, *args):
        conn = self.connection()
        updating = f""
        for f in self.fields: updating += f"{f} = ?,"
        updating = updating[:-1]
        id = args[0]
        sql = f"Update {self.base} set {updating} where id = {id}"
        columnValues = args[1:]
        conn.execute(sql, columnValues)
        print(f"\n{args} Fila #{id} actualizada")
        conn.commit()
        conn.close()
    
if __name__ == '__main__':
    os.system('clear')

    # crea o abre
    alumnos = Database("Persona", "nombre", "fecha_nac") 

    # agrega filas
    alumnos.insert("Juan", "2001-02-02")
    for i in range(3):
        alumnos.insert(f"Nombre {i+1}", f"200{i}-01-01")    
    alumnos.insert("Pipo", "1991-02-03")
    alumnos.insert("Luis", "2111-02-04")

    # borra fila 1
    alumnos.delete(1)

    # actualiza fila 2
    alumnos.update(2, "Quico", "1987-11-11")
    
    # lee todas las filas
    data = alumnos.select()
    
    # muestra todas las filas
    pprint(data, indent=2)