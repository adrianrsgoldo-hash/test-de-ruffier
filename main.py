from PyQt5.QtWidgets import QApplication
from clases.ventana_bienvenida import VentanaBienvenida

if __name__ == "__main__":
    app = QApplication([])
    ventana = VentanaBienvenida()
    ventana.show()
    app.exec_()