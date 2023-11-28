import sys

from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QLabel, QDesktopWidget, QMainWindow, QHBoxLayout, QVBoxLayout, QDialog, \
    QDialogButtonBox, QPushButton


class Ventana6(QMainWindow):

    # Hacer el método de construccién de la ventana
    def __init__(self, parent=None):
        super(Ventana6, self).__init__(parent=parent)

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




if __name__ == '__main__':
    # hacer que la aplicacion se genere
    app = QApplication(sys.argv)

    # creamos un objeto de tipo ventana con el nombre de ventana 1
    ventana = Ventana6()

    # hacer que el objeto ventana 1 se vea
    ventana.show()

    # para terminar la aplicacion
    sys.exit(app.exec_())