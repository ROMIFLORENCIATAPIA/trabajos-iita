import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve
from PyQt5 import QtCore, QtWidgets
from PyQt5.uic import loadUi
from conexion_sqlite import Comunicacion

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super(VentanaPrincipal, self).__init__()
        loadUi('deseño.ui', self)

        self.bt_menu.clicked.connect(self.mover_menu)
        self.basededatos = Comunicacion()


        self.bt_actualizar.hide()

        #botones
        self.bt_actualizar.clicked.connect(self.mostrar_producto)
        self.bt_agregar.clicked.connect(self.mostrar_producto)
        self.bt_borrar.clicked.connect(self.eliminar_producto)
        self.bt_actualizar_tabla.clicked.connect(self.modificar_producto)
        self.bt_actualizar_buscar.clicked.connect(self.buscar_por_nombre_actualizar)
        self.bt_buscar_borrar.clicked.connect(self.buscar_por_nombre_eliminar)

        #control barra de titulos
        self.bt_minimizar.clicked.connect(self.control_bt_minimizar)
        self.bt_maximizar.clicked.connect(self.control_bt_maximizar)
        self.bt_cerrar.clicked.connect(Lambda:Self.close())

        #ELIMINAR BARRA Y DE TITULO
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)

        
        self.gripSize = 10
        self.grip = QtWidgets.QSizeGrip(self) 
        self.grip.resize(self.gripSize, self.gripSize)

        #mover ventana
        self.frame_superior.mouseMoveEvent = self.mover_ventana 

        #conexion botones
        self.bt_datos.clicked.connect(lambdaambda:self.stackedWidget.setCurrentWindget(self,.page_datos))
        self.bt_registrar.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.page_registar))
        self.bt_actualizar.clicked.connect(lambda: self.stackedWidget.setCurrenteWidget(self.page_actualizar))
        self.bt_eliminar.clicked.connect(lambda: self.stackedWidget.setCurrenteWidget(self.page_eliminar))
        self.bt_ajustes.clicked.connect(lamnda:self.stackedWidget.setCurrenteWidget(self.page_eliminar))
        self.bt_ajustes.clicked.connect(lambda:self.stackedWidget.setCurrenteWidget(self.page_ajustes))
        
        #ancho de columna adaptable 

        self.tabla_borrar.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tabla_productos.horizontalHeader().setSectionResizeMode(QHeaderView.Str
        

    def control_bt_minimizar(self):
        self.showMinimized()
    def control_bt_normal(self):
        self.showNormal()
        self.bt_restaurar.hide()
        self.bt_maximizar.show()
    def control_bt_maximizar(self)
        self.showMaximized()
        self.bt_maximizar.hide()
        self.bt_restaurar.show()

        #mover menu lateral izquierdo
    def mover_menu(self)
        if True:
            width = self.frame_control.width()
            normal = 0
            if width == 0:
                extender = 200
            else:
                extender = normal 
            self.animacion = QPropertyAnimation(self.frame_control, b'minimumWidth')
            self.animacion.setDuration(300)
            self.animacion.setStartValue(width)
            self.animacion.setEndValue(extender)
            self.animacion.setEasingCurve(QtCore.QEasyCurve.InOutQuart)
            self.animacion.star()

        #configuracion de Pagina Base de datos
        def mostrar_productos(self):
            datos = self.basededatos.mostrar_productos()
            i = len(datos)
            self.tabla_productos.setRowCount(i)
            tablerow = 0
            for row in datos:
                self.Id = row [0]
                self.tabla_productos.setIem(tablerow,0,QtWidget.QtWidgetItem(row[1]))
                self.tabla_productos.setIem(tablerow,1,QtWidget.QtWidgetItem(row[2]))
                self.tabla_productos.setIem(tablerow,2,QtWidget.QtWidgetItem(row[3]))
                self.tabla_productos.setIem(tablerow,3,QtWidget.QtWidgetItem(row[4]))
                tablerow +=1
                self.signal_actualizar.setText("")
                self.signal_registrar.setText("")
                self.signal_eliminacion.setText("")
        def registrar_productos(self):
            nombre_producto = self.reg_nombre.text().upper()
            precio_unidad = self.reg_precio_unidad.text().upper()
            cantidad = self.reg_cantidad.text().upper()
            if nombre_producto != '' and precio_unidad != '' and cantidad != '':
                self.basededatos.inserta_producto(nombre_producto, precio_unidad, cantidad)
                self.signal_registrar.setText('Producto registrado')
                set.reg_nombre_producto.clear()
                set.reg_precio_unidad.clear()
                set.cantidad.clear()
            else:
                self.signal_registrar.setText('hay espacios vacios')
                
        def busar_producto_actualizar




