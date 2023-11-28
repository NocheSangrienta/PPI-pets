from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QFontDatabase, QFont
from PyQt5.QtWidgets import QMainWindow, QDesktopWidget, QApplication, QWidget, QLabel, QVBoxLayout, QScrollArea, \
    QGridLayout, QButtonGroup, QPushButton

from sextaVentana import Ventana6
import math

import sys


class Ventana2(QMainWindow):


    # Metodo constructor de la ventana
    def __init__(self,parent=None):
        super(Ventana2, self).__init__(parent=parent)

        # Poner el titulo:
        self.setWindowTitle("Ventana clase6")

        # ponemos el color de fondo de la ventana
        self.setStyleSheet("background-color: #7BA4FC;")

        # Estableciendo las propiedades de ancho y alto
        self.ancho = 700
        self.alto = 500

        # Establecer el tamaño de la ventana:
        self. resize(self.ancho, self.alto)

        # Estas lineas hacen que la ventana se vea en el centro:
        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        # Para que la ventan no se pueda cambiar de tamaño
        # Se fija el ancho y el alto
        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        # Creamos una ventana interna
        self.interna = QWidget()
        self.interna.setContentsMargins(20, 20, 20, 20)

        # Establecemos la ventana interna como la ventana central
        self.setCentralWidget(self.interna)

        # Definimos el layout de la ventana interna
        self.vertical = QVBoxLayout()

        # Hacemos el letrero
        self.letrero1 = QLabel()

        # Le escribimos el texto
        self.letrero1.setText("Paseadores Disponibles")

        # Le asignamos el tipo de letra
        self.letrero1.setFont(QFont("Showcard Gothic", 30))

        # Centramos el texto
        self.letrero1.setAlignment(Qt.AlignCenter)

        # Le ponemos color de fondo, color de texto y margenes al letrero
        self.letrero1.setStyleSheet("background-color: #A2BFFD; color: #000000; padding: 30px;"
                                    "border:solid; border-width:5px; border-color:#000000;"
                                    "border-radius:10px; margin-bottom:50px;")

        # Ponemos de primero el letrero
        self.vertical.addWidget(self.letrero1)

        # ponemos un espacio despues
        self.vertical.addStretch()

        # Creamos un scroll
        self.scrollArea = QScrollArea()

        # Hacemos que el scroll se adapte a diferentes tamaños
        self.scrollArea.setWidgetResizable(True)

        # Creamos uan ventana contenedora para la cuadricula
        self.contenedora = QWidget()

        # Vamos a crear un layout de grid para poner una cuadricula de opciones
        self.cuadricula = QGridLayout(self.contenedora)

        # Metemos la ventana contenedora en scroll
        self.scrollArea.setWidget(self.contenedora)

        # Metemos en el layout vertical el scroll
        self.vertical.addWidget(self.scrollArea)

        # Ejemplo numero de elementos
        self.numeroElementos = 7

        # Contador de elementos para mostrar en la cuadricula
        self.contador = 0

        self.elementosPorColumna = 3

        # Redondeamos al entero superior + 1, mostraremos 3 columnas por fila
        # Por eso dividimos por 3
        self.numeroFilas = math.ceil(self.numeroElementos / self.elementosPorColumna) + 1

        # Dejar de ultimo
        # Establecer el layout de la ventana interna
        self.interna.setLayout(self.vertical)

        # Tenemos que agrupar todos los bontones en una propiedad
        self.botones = QButtonGroup()

        # Definimos que self.botones debe estar enterado de lo que hagan todos los bontones
        self.botones.setExclusive(False)

        for fila in range(1, self.numeroFilas):
            for columna in range(1, self.elementosPorColumna+1):
                # Validamos que estamos ingresando la cantidad exacta
                 if self.contador < self.numeroElementos:
                    # En cada celda de la ventana va una cuadricula
                    self.ventanaAux = QWidget()
                    # Se determina su alto y su ancho
                    self.ventanaAux.setFixedHeight(200)
                    self.ventanaAux.setFixedWidth(200)

                    # Creamos un layout vertical para cada elemento en la cuadricula
                    self.verticalCuadricula = QVBoxLayout()

                    # Creamos un label para soportar la imagen
                    self.labelImagen = QLabel()
                    # Establecemos el ancho del label
                    self.labelImagen.setFixedWidth(130)
                    # Establecemos el alto del label
                    self.labelImagen.setFixedHeight(130)
                    # Definimos la imagen
                    self.imagen = QPixmap('imagenes/ama.jpg')
                    # Metemos la imagen el el label
                    self.labelImagen.setPixmap(self.imagen)
                    # Establecemos que queremos escalar la imagen
                    self.labelImagen.setScaledContents(True)

                    # Metemos el label el el layout vertical que tiene la cuadricula
                    # En la fila y la columna actual
                    self.verticalCuadricula.addWidget(self.labelImagen)

                    # Agregamos un espacio en blanco
                    self.verticalCuadricula.addStretch()

                    # creamos un label indicando el nombre del item
                    self.labelNombre = QLabel('Paseadores.'+ str(self.contador + 1))

                    # Le asignamos el tipo de letra
                    self.labelNombre.setFont(QFont("Showcard Gothic", 10))

                    # Metemos el label en el layout para que se vea
                    self.verticalCuadricula.addWidget(self.labelNombre)

                    # Agregamos un espacio en blanco
                    self.verticalCuadricula.addStretch()

                    # Creamos un boton
                    self.botonAccion = QPushButton('Ir a ' + str(self.contador + 1))
                    self.botonAccion.clicked.connect(self.metodo_accion_boton)

                    # Le asignamos el tipo de letra
                    self.botonAccion.setFont(QFont("Comic Sans MS", 8))

                    # Establecemos el ancho del boton
                    self.botonAccion.setFixedWidth(137)

                    # Metemos el label en el layout para que se vea
                    self.verticalCuadricula.addWidget(self.botonAccion)

                    # Agregamos el boton al grupo, con su contador como id
                    self.botones.addButton(self.botonAccion, self.contador + 1)

                    # Agregamos un espacio en blanco
                    self.verticalCuadricula.addStretch()

                    # A la ventana le asignamos el layout vertical
                    self.ventanaAux.setLayout(self.verticalCuadricula)

                    # A la cuadricula le agregamos la ventana en la fila y la columna actual
                    self.cuadricula.addWidget(self.ventanaAux, fila, columna)

                    # Aumentamos el contador
                    self.contador += 1

        # Establecemos el metodo para que funcionen todos los botones
        self.botones.idClicked.connect(self.metodo_accion_boton)

    def metodo_accion_boton(self, idBoton):

        self.ventanaServicios = Ventana6()
        self.ventanaServicios.show()



