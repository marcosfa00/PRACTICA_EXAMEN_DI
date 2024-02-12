import sys

from PyQt6.QtGui import QColor, QIcon
# importamos del pyqt6 los elementos que nos importa -> ventana principal, boton
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout,
    QLineEdit, QHBoxLayout, QTableView, QWidget, QComboBox, QCheckBox
)

from PyQt6.QtCore import Qt, QAbstractTableModel, QModelIndex


class ModeloTaboa(QAbstractTableModel):
    def __init__(self, table, headerData):
        super().__init__()
        self.table = table
        self.headerData = headerData

    def rowCount(self, index):
        return len(self.table)

    def columnCount(self, index):
        return len(self.table[0])

    # to fill the table
    def data(self, index, role):
        if index.isValid():
            if role == Qt.ItemDataRole.EditRole or role == Qt.ItemDataRole.DisplayRole:
                return self.table[index.row()][index.column()]
            if role == Qt.ItemDataRole.ForegroundRole:
                if self.table[index.row()][3]:
                    return QColor(Qt.GlobalColor.red)

    # to edit the table
    def setData(self, index, value, role):
        if role == Qt.ItemDataRole.EditRole:
            self.table[index.row()][index.column()] = value
            return True
        return False

    def flags(self, index):
        return Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsEditable | Qt.ItemFlag.ItemIsSelectable

    def headerData(self, section, orientation, role):
        if role == Qt.ItemDataRole.DisplayRole:
            if orientation == Qt.Orientation.Horizontal:
                return self.headerData[0][section]
            '''
            elif orientation == Qt.Orientation.Vertical:
                return section + 1
            '''
