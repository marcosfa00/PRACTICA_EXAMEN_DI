'''
Bien, tras crear nuestra base de datos SQL con ciertos inserts, podemos empezar a bisualizar esto ddatos en una tabla
Esta tabla la crearemos aquí,
para mostrar esto no hay que crear un modelto de Tabla

procedemos ha ahcer los imports necesarios

'''

import sys

from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QPixmap
from PyQt6.QtSql import QSqlTableModel, QSqlDatabase
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QPushButton,
                             QGridLayout, QVBoxLayout, QHBoxLayout, QLabel, QCheckBox, QListWidget,
                             QComboBox, QFrame, QSlider, QGroupBox, QTableWidget, QTableView, QLineEdit)


class VentanaTablaSQL(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('TABLA SQL')

        main_window = QVBoxLayout()

        parteTabla = QHBoxLayout()

        parteBotones = QHBoxLayout()

        main_window.addLayout(parteTabla)
        main_window.addLayout(parteBotones)


        # lo primero es conectarnos a nuestra base de datos
        myDataBase = QSqlDatabase("QSQLITE") # aquí indicamos que el modelo de la base d edatos es de tipo SQLite
        myDataBase.setDatabaseName("database.dat")# aquí indicamos el nomrbe de nuesro archivo
        # provedemos a abrir la conexion con la base de datos
        myDataBase.open()

        # procedemos a crear la tabla SQL
        table  = QTableView()
        # ahora toca crear el modelo de la tabla
        model = QSqlTableModel(db=myDataBase) # este ya es un modelo por defecto
        #como se va a editar nuestra tabla:
        # self.modelo.setEditStrategy(QSqlTableModel.EditStrategy.OnFieldChange)
        # self.modelo.setEditStrategy(QSqlTableModel.EditStrategy.OnRowChange)
        model.setEditStrategy(QSqlTableModel.EditStrategy.OnManualSubmit)
        # indicamos el layout de nuestra tabla
        layoutTabla = QVBoxLayout()

        table.setModel(model) # indicamos al QTableView la tabla que se va a ver

        model.setTable("usuarios") # idnicamos que tabla de la base de datos vamos a visualizar
        # hacemos la consulta
        model.select()

        parteTabla.addWidget(table)

        #mostramos la ventana
        contenedor = QWidget()
        contenedor.setLayout(main_window)
        self.setCentralWidget(contenedor)
        self.setMinimumSize(QSize(500, 300))
        self.show()

if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = VentanaTablaSQL()
    aplicacion.exec()

