import sys

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QPushButton,
                             QGridLayout, QVBoxLayout, QHBoxLayout, QLabel, QCheckBox, QListWidget,
                             QComboBox, QFrame, QSlider, QGroupBox, QTableWidget, QTableView, QLineEdit)

from PracticandoTabla import MyTable

# a continuacion vamos a crear una ventana donde se vea nuestra tabla correctamente
class VentanaTabla(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Ventana con Tabla ')
        self.setFixedSize(550, 500)

        vbox = QVBoxLayout()

        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()

        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)

        # a continuación creremos unos cuantos botones
        botonera = QWidget()
        layoutbotonera = QVBoxLayout()

        # declaramos los botones
        button1 = QPushButton('añadir')
        button1.clicked.connect(lambda: self.addToTable(txtName,txtApellido,txtEdad,txtSexo,checkBoxWork,table))
        button2 = QPushButton('editar')

        button3 = QPushButton('boton3')
        button4 = QPushButton('boton4')

        # añadimos los botones al Layout

        layoutbotonera.addWidget(button1)
        layoutbotonera.addWidget(button2)
        layoutbotonera.addWidget(button3)
        layoutbotonera.addWidget(button4)

        # ahora añadimos el layour al widget

        botonera.setLayout(layoutbotonera)

        # ahora añadimos al layour principal la botonera
        hbox1.addWidget(botonera)


        #debajo de estos botones crearemos nuestra tabla
        #para ello debemos crear una matriz 2D
        self.datosTabla =[
            # aquí dentro se definen lso datos a poner en una tabla

            #la primera fila siempre van a ser los campso de las columnas
            ['Nombre', 'Apellidos', 'edad','sexo','trabajando'],
            # a continuacion se definen los datos que van en estas columnas
            ['Marcos', 'F. Avendaño', 23,'Macho Alfa', True],
            ['FERNANDO', 'ALONSO', 33,'Macho Alfa', True],
            ['Sara', 'Gonzalez', 23,'Femia', True],
            ['Women', 'Cualquiera', 23,'Mujer', False],

        ]

        # DECLARACION DE UNA TABLA
        cuadradoTabla = QWidget()
        layoutCuadrado = QHBoxLayout()

        # creamos el elemento tabla
        table = QTableView()
        # indicamos el modelo de la tabla
        modelo = MyTable(self.datosTabla)#le pasamos los datos a nuestro modelo
        # la indicamos a nuestra tabla que tendrá este modelo
        table.setModel(modelo)

        # añladimos la tabla al layout
        layoutCuadrado.addWidget(table)

        cuadradoTabla.setLayout(layoutCuadrado)

        hbox2.addWidget(cuadradoTabla)

        # a continuación añadiremos los textfields para poder escribir los nuevos elementso
        textos = QWidget()
        layoutTextos = QVBoxLayout()

        ## creamos los txtFields
        # ['Nombre', 'Apellidos', 'edad','sexo','trabajando'],
        txtName = QLineEdit()
        txtApellido = QLineEdit()
        txtEdad = QLineEdit()
        txtSexo = QLineEdit()
        checkBoxWork = QCheckBox('Trabajando')

        layoutTextos.addWidget(txtName)
        layoutTextos.addWidget(txtApellido)
        layoutTextos.addWidget(txtEdad)
        layoutTextos.addWidget(txtSexo)
        layoutTextos.addWidget(checkBoxWork)

        textos.setLayout(layoutTextos)

        hbox1.addWidget(textos)




        container = QWidget()
        container.setLayout(vbox)

        # Establecemos el contenedor como el widget central
        self.setCentralWidget(container)

        # Mostramos la ventana
        self.show()

    # ahroa vamos a programar las dfunciones del boton añadir elementos

    def addToTable(self,nombre,apellido,edad,sexo,trabajando,table):
        name = nombre.text()
        apell = apellido.text()
        age = edad.text()
        sex = sexo.text()
        working = False
        nombre.clear()
        apellido.clear()
        edad.clear()
        sexo.clear()
        trabajando.setChecked(False)
        if trabajando.isChecked():
            working = True

        nuevo_campo =  [name, apell, age, sex, working]
        self.datosTabla.append(nuevo_campo)
        # hasta ahora no se muesra el cambio porque hay que actualizar los datos de la tabla:
        # Actualiza el modelo de la tabla
        modelo = MyTable(self.datosTabla)
        table.setModel(modelo)











if __name__ == "__main__":
    aplicacion = QApplication(sys.argv)
    ventana = VentanaTabla()
    sys.exit(aplicacion.exec())


