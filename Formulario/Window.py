import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (
    QMainWindow, QApplication, QVBoxLayout, QWidget, QHBoxLayout, QLabel, QCheckBox, QListWidget, QPushButton,
    QTabWidget, QTableView
)
from ModeloTabla import ModeloTaboa


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Window Formulario')
        self.resize(800, 600)

        # Creamos un QVBoxLayout como el diseño principal
        main_layout = QVBoxLayout()

        # Creamos dos QHBoxLayout para los elementos
        h_box1 = QHBoxLayout()
        h_box2 = QHBoxLayout()

        # Añadimos los QHBoxLayout al QVBoxLayout principal
        main_layout.addLayout(h_box1)
        main_layout.addLayout(h_box2)

        # Creamos un QWidget para el primer elemento (Disco)
        widget_disco = QWidget()

        # Creamos un QVBoxLayout para el primer elemento
        layout_disco = QVBoxLayout(widget_disco)

        # Añadimos un QLabel y un QCheckBox al QVBoxLayout del primer elemento
        image_label = QLabel("Animado")
        image_label.setPixmap(QPixmap("icons/checked.png"))
        check_box = QCheckBox("Disco")

        layout_disco.addWidget(image_label, alignment=Qt.AlignmentFlag.AlignTop)
        layout_disco.addWidget(check_box, alignment=Qt.AlignmentFlag.AlignTop)

        # Añadimos el QWidget del primer elemento al primer QHBoxLayout
        h_box1.addWidget(widget_disco)

        widget_Lista = QWidget()
        LayoutLista = QVBoxLayout(widget_Lista)

        # Creamos los componentes que van a ir en la lista
        lista = QListWidget()

        # añadimos la lista al Layout
        LayoutLista.addWidget(lista)

        ## añadimos al horizontalBox principal la lista

        h_box1.addWidget(widget_Lista)


        # Ahora vamos a crear los botones:
        widgetBotones = QWidget()
        layoutBotones = QVBoxLayout(widgetBotones)

        Btn1 = QPushButton("Boton")
        Btn2 = QPushButton("Boton")
        Btn3 = QPushButton("Boton")
        Btn4 = QPushButton("Boton")
        Btn5 = QPushButton("Boton")
        Btn6 = QPushButton("Boton")

        layoutBotones.addWidget(Btn1)
        layoutBotones.addWidget(Btn2)
        layoutBotones.addWidget(Btn3)
        layoutBotones.addWidget(Btn4)
        layoutBotones.addWidget(Btn5)
        layoutBotones.addWidget(Btn6)

        h_box1.addWidget(widgetBotones)
        # mostrar la tabla
       # widgetTabla = QWidget()  esto es innecesario
       # layoutTabla = QVBoxLayout(widgetTabla)

        # datos de la tabla
        # Creamos una lista de listas para los datos de la tabla
        self.table = [
            ["Ana Pérez", "1234Y", "Mujer", True],
            ["Paco Pecas", "6789I", "Hombre", False],
            ["Roque Vila", "4567H", "Hombre", True],
            ["Luis Yánez", "4321W", "Hombre", False]
        ]

        # Cabecera de la tabla
        headerData = ["Name", "DNI", "Gender", "Dead?"]

        tabla = QTableView()  # Widget de la tabla
        layoutTabla = QVBoxLayout(tabla)
        modeloDeTabla = ModeloTaboa(self.table, headerData)

        # Configuramos la tabla con el modelo
        tabla.setModel(modeloDeTabla)

        # Añadimos la tabla al layout


        # Añadimos la tabla al layout




        h_box1.addWidget(tabla)

        # Creamos un contenedor y le asignamos el QVBoxLayout principal
        container = QWidget()
        container.setLayout(main_layout)

        # Establecemos el contenedor como el widget central
        self.setCentralWidget(container)

        # Mostramos la ventana
        self.show()

if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = Window()
    sys.exit(aplicacion.exec())
