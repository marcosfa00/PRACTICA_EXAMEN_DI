import sys
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (
    QMainWindow, QApplication, QVBoxLayout, QWidget, QHBoxLayout, QLabel, QCheckBox, QListWidget, QPushButton,
    QTabWidget, QTableView, QComboBox, QSlider
)


class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('prcticando interfaces')
        ### EMpezamos a crar la ven tana

        main_layout = QVBoxLayout()  # los elementos se colocan en vertical

        parte1 = QHBoxLayout()
        parte2 = QHBoxLayout()
        parte3 = QHBoxLayout()

        main_layout.addLayout(parte1)
        main_layout.addLayout(parte2)
        main_layout.addLayout(parte3)

        # Parte cuadrado
        parteIcono = QWidget()

        LayoutIcono = QVBoxLayout()

        # Elementos cuadrado
        labelIcono = QLabel("Icono")
        labelIcono.setPixmap(QPixmap("icono.png"))

        checkBox = QCheckBox("Animado")

        # añadimos los elementos al layout

        LayoutIcono.addWidget(labelIcono)
        LayoutIcono.addWidget(checkBox)

        parteIcono.setLayout(LayoutIcono)

        parte1.addWidget(parteIcono)

        # Parte Lista
        widgetLista = QWidget()
        layoutLista = QVBoxLayout()

        cuadradoLista = QListWidget()

        layoutLista.addWidget(cuadradoLista)

        widgetLista.setLayout(layoutLista)

        parte1.addWidget(widgetLista)

        # Parte botones
        ParteBotones = QWidget()
        layoutBotones = QVBoxLayout()

        botonesMedio = QWidget()
        layoutBMedio = QHBoxLayout()

        botonMedio = QPushButton("Saltar")
        comboBox = QComboBox()

        layoutBMedio.addWidget(botonMedio)
        layoutBMedio.addWidget(comboBox)

        botonesMedio.setLayout(layoutBMedio)

        # botones
        boton1 = QPushButton("Añadir pista a reproducir")
        boton1.clicked.connect(lambda: self.addElement(cuadradoLista) )

        boton2 = QPushButton("Subir")
        boton3 = QPushButton("Bajar")
        # aqui va BotonesMedio
        boton5 = QPushButton("Abrir")
        boton6 = QPushButton("reproducir")
        boton7 = QPushButton("Guardar")
        boton8 = QPushButton("Eliminar")

        layoutBotones.addWidget(boton1)
        layoutBotones.addWidget(boton2)
        layoutBotones.addWidget(boton3)
        layoutBotones.addWidget(botonesMedio)
        layoutBotones.addWidget(boton5)
        layoutBotones.addWidget(boton6)
        layoutBotones.addWidget(boton7)
        layoutBotones.addWidget(boton8)

        ParteBotones.setLayout(layoutBotones)

        parte1.addWidget(ParteBotones)

        # Parte 2

        boxTipoSonido = QWidget()
        layoutSonito = QVBoxLayout()

        # creamos los elementos

        sonido = QLabel("Sonido")
        ritmo = QLabel("Ritmo")
        volumen = QLabel("Volumen")
        Formato = QLabel("Formato")
        salidaAudio = QLabel("Salida Audio")

        # añadimos los elementos al Layout

        layoutSonito.addWidget(sonido)
        layoutSonito.addWidget(ritmo)
        layoutSonito.addWidget(volumen)
        layoutSonito.addWidget(Formato)
        layoutSonito.addWidget(salidaAudio)

        boxTipoSonido.setLayout(layoutSonito)

        parte2.addWidget(boxTipoSonido)

        # parte selección

        boxSeleccionSonido = QWidget()
        seleccionLayout = QVBoxLayout()

        elementos = ['', 'Selecciona', 'hola', 'Que', 'tal']

        # creanos los elementos
        comboboxSonido = QComboBox()
        comboboxSonido.addItems(elementos)
        comboboxSonido.setCurrentIndex(0)

        sliderRitmo = QSlider(Qt.Orientation.Horizontal)

        sliderVolumen = QSlider()
        sliderVolumen.setOrientation(Qt.Orientation.Horizontal)

        comboFormato = QComboBox()
        comboFormato.addItem('')

        comboSalidaAudio = QComboBox()

        # aladimos elementos al layout

        seleccionLayout.addWidget(comboboxSonido)
        seleccionLayout.addWidget(sliderRitmo)
        seleccionLayout.addWidget(sliderVolumen)
        seleccionLayout.addWidget(comboFormato)
        seleccionLayout.addWidget(comboSalidaAudio)

        boxSeleccionSonido.setLayout(seleccionLayout)

        parte2.addWidget(boxSeleccionSonido)

        ## CONTENEDOR PRINCIPAL
        container = QWidget()
        container.setLayout(main_layout)

        # Establecemos el contenedor como el widget central
        self.setCentralWidget(container)

        # Mostramos la ventana
        self.show()

    def addElement(self, lista):
        # Pedir datos por consola antes de agregar a la lista
        nuevo_elemento = input("Introduce el nuevo elemento: ")
        lista.addItem(nuevo_elemento)

if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = Ventana()
    sys.exit(aplicacion.exec())
