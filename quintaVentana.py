import sys

from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QDesktopWidget, QMainWindow, QPushButton



class Ventana5(QMainWindow):

    # Hacer el método de construccién de la ventana
    def __init__(self, anterior):
        super(Ventana5, self).__init__(anterior)

        self.ventanaAnterior = anterior

        # Poner el titulo:
        self.setWindowTitle("PPI pets")

        # Estableciendo las propiedades de ancho y alto
        self.ancho = 700
        self.alto = 500
        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        # Estas Lineas hacen que la ventana se vea en el centro:
        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        self.fondo = QLabel()
        self.imagenFondo = QPixmap("Imagenes/mj.jpg")
        self.fondo.setPixmap(self.imagenFondo)
        self.fondo.setScaledContents(True)
        self.setCentralWidget(self.fondo)

        self.ayudas = QPushButton(self)
        self.ayudas.setText("Atras")
        self.ayudas.setFixedWidth(200)
        self.ayudas.setStyleSheet("background-color: #74C5E3;")
        self.ayudas.move(470, 450)
        self.ayudas.clicked.connect(self.ir_atras)

    def ir_atras(self):
        self.hide()
        self.ventanaAnterior.show()
if __name__ == '__main__':
    # hacer que la aplicacion se genere
    app = QApplication(sys.argv)

    # creamos un objeto de tipo ventana con el nombre de ventana 1
    ventana = Ventana5()

    # hacer que el objeto ventana 1 se vea
    ventana.show()

    # para terminar la aplicacion
    sys.exit(app.exec_())