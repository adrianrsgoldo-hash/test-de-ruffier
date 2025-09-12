from PyQt5.QtWidgets import QWidget

class VentanaBase(QWidget):
    def __init__(self, titulo="Ventana Base", ancho=800, alto=600):
        super().__init__()
        self.setWindowTitle(titulo)
        self.setFixedSize(ancho, alto)
        self.centrar()
        
    def centrar(self):
        pantalla = self.frameGeometry()
        centro_pantalla = self.screen().availableGeometry().center()
        pantalla.moveCenter(centro_pantalla)
        self.move(pantalla.topLeft())
        
    