import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (
    QMainWindow, QApplication, QVBoxLayout, QWidget, QHBoxLayout, QLabel, QCheckBox, QListWidget, QPushButton,
    QTabWidget, QTableView
)


class VentanaAnxo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Anxo_gamer.com')
        self.resize(800, 600)

        cajaprincipal = QVBoxLayout()

        parte1 = QWidget()
        horizontalBotones = QHBoxLayout()
        parte1.setLayout(horizontalBotones)

        checkBox = QCheckBox('Animado')
        horizontalBotones.addWidget(checkBox)

        cajaprincipal.addWidget(parte1)  # Cambiado: agregado parte1 directamente a cajaprincipal
        lista = QListWidget()
        listavertical = QVBoxLayout()
        listavertical.addWidget(lista)

        cajaprincipal.addLayout(listavertical)

        container = QWidget()
        container.setLayout(cajaprincipal)


        # Establecemos el contenedor como el widget central
        self.setCentralWidget(container)

        # Mostramos la ventana
        self.show()


if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = VentanaAnxo()
    sys.exit(aplicacion.exec())