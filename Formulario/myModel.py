# primero haremos los Imports

import sys

from PyQt6.QtCore import Qt, QAbstractListModel
from PyQt6.QtGui import QColor, QIcon, QPixmap
# importamos del pyqt6 los elementos que nos importa -> ventana principal, boton
from PyQt6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout, QWidget,
                             QHBoxLayout, QGridLayout, QLabel, QCheckBox, QListView, QPushButton, QSizePolicy,
                             QComboBox, QFrame, QGroupBox, QSlider, QRadioButton, QLineEdit)


class myModel(QAbstractListModel):
    def __init__(self, tasks=None):  # Constructor de la clase
        super().__init__()
        # el constructor espera una lista de tareas, si no se poporciona se añade una Lista vacía
        self.task = tasks or []  # or indica que si no se proporciona una lista entonces se añade una vacía

    def data(self, index, role):
        '''
        :param Roles:
            - DisplayRole: el texto a ser mostrado en la tabla
            - DecorationRole: el icono de la tabla
            - EditRole: el texto a ser editado en la tabla

        '''

        if role == Qt.ItemDataRole.DisplayRole:
            # la barra baja _  es una convencion para indicar que no usamos etsa variable
            _, text = self.task[index.row()]
            return text
        elif role == Qt.ItemDataRole.DecorationRole:
            state, _ = self.task[index.row()]
            if state:
                return QIcon('icons/checked.png')
            else:
                return QIcon('icons/unchecked.png')

    def rowCount(self, index):
        return len(self.task)
