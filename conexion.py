import sqlite3

class Conexion():    # Esta es la conexion
    def __init__(self) -> None:
        try: 
            self.con = sqlite3.connect("banco.db")
            self.crearTablas()
        except Exception as ex:
            print(ex)
    
    def crearTablas(self): # Creamos la tabla usuarios
        sql_create_tabla1 =""" CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY AUTOINCREMENT, nombre TEXT, usuario TEXT UNIQUE, clave TEXT)"""
        cur = self.con.cursor()
        cur.execute(sql_create_tabla1)
        cur.close()
        self.crearAdmin()

    def crearAdmin(self):
        try:
            sql_insert =""" INSERT INTO usuarios VALUES(null, '{}', '{}', '{}')""".format("Admin", "admin","admin2024")
            cur = self.con.cursor()
            cur.execute(sql_insert)
            self.con.commit()
        except Exception as ex:
            print("usuario Admin ya creado: ", ex)

con = Conexion()