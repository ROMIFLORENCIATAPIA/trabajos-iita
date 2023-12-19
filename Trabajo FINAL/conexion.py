import sqlite3

class Comunicacion():
    def __init__(self):
        self.conexion = sqlite3.connect('basededatos.db')

    def inserta_producto(self,nombre_producto, precio_unidad, cantidad):
        cursor = self.conexion.cursor()
        bd = '''INSERT INTO tabla_datos (NOMBRE, PRECIO, CANTIDAD)
        VALUES('{}, {}, {}, {}'''.format(nombre_producto,precio_unidad,cantidad)
        cursor.execute(bd)
        self.conexion.comit()
        cursor.close()

    def mostrar_productos(self):
    cursor = self.conexion.cursor()
    bd = "SELECT * FROM tabla_datos "
    cursor.execute(bd)
    registro = cursor.fetchall()
    return registro

    def buscar_producto(self,nombre_producto):
        cursor = self.conexion.cursor()
        bd = '''SELECT * FROM tabla_datos WHERE = {}'''.format(nombre_producto)
        cursor.execute(bd)
        nombreX = cursor.fetchall()
        cursor.close()
        return nombreX
    
    def eliminar_producto(self, nombre_producto):
        cursor = self.conexion.cursor()
        bd = '''DELETE FROM tabla_datos WHERE NOMBRE = {}'''.format(nombre_producto)
        cursor.execute(bd)
        self.conexion.comit()
        cursor.close()

    def actualizar_producto(self, Id,nombre_producto, precio_unidad, cantidad):
        cursor = self.conexion.cursor()
        bd = '''UPDATE tabla_datos SET NOMBRE = '{}', PRECIO = '{}', CANTIDAD = '{}'
         WHERE ID = '{}' '''.format(nombre_producto, precio_unidad, cantidad, Id)
        cursor.execute(bd)
        a = cursor.rowcount
        self.conexion.comit()
        cursor.close()
        return a  
    