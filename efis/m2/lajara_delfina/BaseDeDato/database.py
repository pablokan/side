import sqlite3

# Modificamos algunos parametros...

class Database:
    def __init__(self, tabla, *args) -> None:
        """ Params: Nombre de la base de datos y nombres de los atributos """
        self.tabla = tabla
        self.fields = args
        conn = sqlite3.connect(f"BaseDeDato\Restaurante.db")
        if len(args) != 0:
            sArgs = ""
            for arg in args: sArgs += arg + ", " 
            self.sArgs = sArgs[:-2]
            # print(f'Debugging ######## {self.sArgs=} #########')
            self.params = params = f"('id' integer primary key autoincrement, {self.sArgs})"
            try:
                sql = f"create table {tabla} {params}"
                #print(sql)
                conn.execute(sql)
                #print(f"Se creó la tabla {base}")                        
            except sqlite3.OperationalError:
                pass
        conn.close()

    def insert(self, *args):
        conn = sqlite3.connect(f"BaseDeDato\Restaurante.db")
        if self.sArgs.startswith('id'): self.sArgs = self.sArgs[4:]
        sql = f"INSERT INTO {self.tabla}({self.sArgs}) VALUES {args}"
        # print(sql)
        conn.execute(sql)
        conn.commit()
        conn.close()

    def selectBuscarCliente(self,param,dato):
        conn = sqlite3.connect(f"BaseDeDato\Restaurante.db")
        rs = conn.execute(f"SELECT * FROM {self.tabla} WHERE {param} = '{dato}'")
        lista = []
        for r in rs: 
            lista.append(r)
        conn.close()
        return lista  

    def selectBuscarComidas(self,param,dato):
        conn = sqlite3.connect(f"BaseDeDato\Restaurante.db")
        rs = conn.execute(f"SELECT * FROM {self.tabla} WHERE {param} = '{dato}'")
        lista = []
        for r in rs: 
            lista.append(r)
        conn.close()
        return lista  

    def select(self):
        conn = sqlite3.connect(f"BaseDeDato\Restaurante.db")
        rs = conn.execute(f"SELECT * FROM {self.tabla}")
        lista = []
        for r in rs: 
            lista.append(r)
        conn.close()
        return lista    
        
    def delete(self, id):
        id = 0 if id=="" else id
        conn = sqlite3.connect(f"BaseDeDato\Restaurante.db")
        sql = f"DELETE FROM {self.tabla} WHERE id={id}"
        #print(sql)
        rs = conn.execute(sql)
        conn.commit()
        conn.close()

    def update(self, *args):
        #id = 0 if id=="" else id
        conn = sqlite3.connect(f"BaseDeDato\Restaurante.db")
        #print(self.fields)
        updating = f""
        for f in self.fields:
            updating += f"{f} = ?,"
        updating = updating[:-1]
        id = args[0]
        sql = f"Update {self.tabla} set {updating} where id = {id}"
        columnValues = args[1:]
        #print(f'Debugging ######## {columnValues=} #########')
        conn.execute(sql, columnValues)
        conn.commit()
        conn.close()

    def ObtenerUltimoRegistro(self):
        conn = sqlite3.connect(f"BaseDeDato\Restaurante.db")
        rs = conn.execute(f"SELECT * FROM {self.tabla} WHERE id=(SELECT max(id) FROM {self.tabla})")
        lista = []
        for r in rs: 
            lista.append(r)
        conn.close()
        return lista

    
