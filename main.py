from PyQt5.QtWidgets import QApplication
from clases.ventana_bienvenida import VentanaBienvenida
from clases.ventana_test import VentanaTest

if __name__ == "__main__":
    app = QApplication([])
    with open("estilos/estilos.qss", "r") as f:
        app.setStyleSheet(f.read())
    ventana = VentanaBienvenida()
    ventana.show()
    app.exec_()
    