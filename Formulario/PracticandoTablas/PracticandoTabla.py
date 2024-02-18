import sys
from PyQt6.QtCore import Qt, QAbstractTableModel
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6.QtWidgets import (
    QMainWindow, QApplication, QVBoxLayout, QWidget, QHBoxLayout, QLabel, QCheckBox, QListWidget, QPushButton,
    QTabWidget, QTableView
)
from PyQt6.QtGui import QColor

from PyQt6.uic.properties import QtGui


# Vamos a crear en esta clase el modelo de la tabla

class MyTable(QAbstractTableModel):
     # Constructor
     # le pasamos como parámetro tabla para mas adelante poder trabajar con el.
    def __init__(self, tabla):
        super().__init__()
        self.tabla = tabla

    # aquí declaramos diferentes Metodos que heredamos de QAbstractTableModel
    def rowCount(self, indice): # esta función devuelve la longitud de las FILAS de latabla actual que estamos utilizando
        return len(self.tabla) # len es lo que equivale en Java al .length

     # esta funcion hace lo mismo que la anterior pero para el número de columnas
    def columnCount(self, indice): # En este caso, asumimos que todas las filas tienen la misma cantidad de columnas y devolvemos la longitud de la primera fila
        return len(self.tabla[0])

    # indice es una posición en la tabla
    # rol indica que vamos ha hacer con la celda seleccionada (editarla, visualizar su contenido....)
    def data(self, indice, rol):
        if indice.isValid():
            # si llegamos a quí indicamos que el indice era valido (es decir que exisyte una fila con ese indice

            if rol == Qt.ItemDataRole.EditRole or rol == Qt.ItemDataRole.DisplayRole:
                # idnica que si el rol indicado es de modo edicion o visualizacion de datos obtenemos
                #el valor de esa celda y lo retornamos
                valor = self.tabla[indice.row()][indice.column()]
                return valor

            # a continuacion se pondra el color de la letra en rojo si la tercera columna de la fila Actual
            # es igual a True
            if rol == Qt.ItemDataRole.ForegroundRole:
                if self.tabla[indice.row()][4]:
                    return QColor("red")

            ## a continuación indicaremos como se cambiará de color el Fondo de la celda
            # en función de ciertos parámetros
            # esta tabla realmente se estructura ya sabiendo los datos que vamos a mostrar
            if rol == Qt.ItemDataRole.BackgroundRole:
                # si el valor de la columna dos de las filas es Hombre, el Fondo se pone verde
                if self.tabla[indice.row()][2]=="Hombre":
                    return QColor("green")

                # si por el contrario es Mujer se pone Rosa
                if self.tabla[indice.row()][3]=="Femia":
                    return QColor("pink")
                # si es otro tipo de especie que se pinte de negro
                if self.tabla[indice.row()][3]=="Macho Alfa":
                    return QColor("Blue")

            # ahora vamos a emplear datos decorativos, cómo Iconos asociados a una celda
            if rol == Qt.ItemDataRole.DecorationRole:
                # ahora preguntamos, si el primer condicional (En este caso solo hay uno, pero podría haber varios) es Verdadero
                if isinstance(self.tabla[indice.row()][indice.column()], bool):
                    if self.tabla[indice.row()][indice.column()]:
                        return QIcon("check.png")
                    else:
                        return QIcon("uncheck.png")

# Otra de las funciones predefinidas dentro de lo que es una tabla son las siguientes
    def setData(self, indice, valor,rol):
        if  rol == Qt.ItemDataRole.EditRole:
            self.tabla[indice.row()][indice.column()] = valor
            return True
        return False


    def flags(self, index):
        if index.row() == 0:
            return Qt.ItemFlag.ItemIsEnabled
        return Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsEditable | Qt.ItemFlag.ItemIsSelectable



## Bien la tabla ya la tenemos definida, ahora toca pasar a la ventana
