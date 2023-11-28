import sys

from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtWidgets import QDesktopWidget, QMainWindow, QApplication, QLabel, QPushButton, QVBoxLayout, QLineEdit, \
    QFormLayout

from quintaVentana import Ventana5
from cuartaVentana import Ventana4
from segundaVentana import Ventana2
from terceraVentana import Ventana3

class Ventana1(QMainWindow):

    # Hacer el método de construccién de la ventana
    def __init__(self, parent=None):
        super(Ventana1, self).__init__(parent=parent)

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





        self.tituloUsuario = QLabel(self)
        self.tituloUsuario.setText("Usuario")
        # Le asignamos el tipo de letra
        self.tituloUsuario.setFont(QFont("Showcard Gothic", 10))
        self.tituloUsuario.move(150, 150)



        self.usuario = QLineEdit(self)
        self.usuario.setStyleSheet("background-color: white;")
        self.usuario.setFixedWidth(200)
        self.usuario.move(300,150)



        self.tituloContrasena = QLabel(self)
        self.tituloContrasena.setText("Contraseña")



        # Le asignamos el tipo de letra
        self.tituloContrasena.setFont(QFont("Showcard Gothic", 10))
        self.tituloContrasena.move(150, 180)







        self.contrasena = QLineEdit(self)
        self.contrasena.setStyleSheet("background-color: white;")
        self.contrasena.setFixedWidth(200)
        self.contrasena.move(300, 180)


        self.ingresar = QPushButton(self)
        self.ingresar.setText("Ingresar")

        self.ingresar.setFixedWidth(200)
        self.ingresar.setStyleSheet("background-color: #74C5E3;")
        self.ingresar.move(100,250)
        self.ingresar.clicked.connect(self.ir_ventana2)




        self.registrarse = QPushButton(self)
        self.registrarse.setText("Registrarse")
        self.registrarse.setFixedWidth(200)
        self.registrarse.setStyleSheet("background-color: #74C5E3;")
        self.registrarse.move(300, 250)
        self.registrarse.clicked.connect(self.ir_ventana3)

        self.registrarse2 = QPushButton(self)
        self.registrarse2.setText("Registrar Paseador")
        self.registrarse2.setFixedWidth(200)
        self.registrarse2.setStyleSheet("background-color: #74C5E3;")
        self.registrarse2.move(300, 280)
        self.registrarse2.clicked.connect(self.ir_ventana4)

        self.ayudas = QPushButton(self)
        self.ayudas.setText("Ayudas")
        self.ayudas.setFixedWidth(200)
        self.ayudas.setStyleSheet("background-color: #74C5E3;")
        self.ayudas.move(470, 450)
        self.ayudas.clicked.connect(self.ir_ventana5)







        self.letrero1 = QLabel(self)
        self.letrero1.setText("Paseos Para perros")
        self.letrero1.setFont(QFont("Andale Mono", 17))
        self.letrero1.setFixedWidth(300)


        #Centramos el Texto
        self.letrero1.setStyleSheet("background-color: #FFFFFF; color: #008845; padding: 50px;"
                                    "border-radius:40px;  margin-botton:50px;")
        self.letrero1.move(180, 50)

    def ir_ventana5(self):
        self.hide()
        self.ventanaAyudas = Ventana5(self)
        self.ventanaAyudas.show()


    def ir_ventana4(self):
        self.hide()
        self.ventanaRegistro2 = Ventana4(self)
        self.ventanaRegistro2.show()


    def ir_ventana3(self):
        self.hide()
        self.ventanaRegistro = Ventana3(self)
        self.ventanaRegistro.show()

    def ir_ventana2(self):
        self.hide()
        self.ventanaSiguiente = Ventana2(self)
        self.ventanaSiguiente.show()


if __name__ == '__main__':
    # hacer que la aplicacion se genere
    app = QApplication(sys.argv)

    # creamos un objeto de tipo ventana con el nombre de ventana 1
    ventana = Ventana1()

    # hacer que el objeto ventana 1 se vea
    ventana.show()

    # para terminar la aplicacion
    sys.exit(app.exec_())