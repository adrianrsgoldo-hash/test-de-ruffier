from PyQt5.QtWidgets import QLabel, QVBoxLayout, QPushButton
from clases.ventana_base import VentanaBase
from clases.ventana_test import VentanaTest
from recursos.instrucciones import instrucciones_bienvenida

class VentanaBienvenida(VentanaBase):
    def __init__(self):
        super().__init__(titulo="Bienvenida", ancho=600, alto=500)
        self.layout = QVBoxLayout()
        #widget
        self.label_bienvenida = QLabel(instrucciones_bienvenida['titulo'])
        self.label_bienvenida.setObjectName("titulo")
        self.layout.addWidget(self.label_bienvenida)
        self.explicacion = QLabel(instrucciones_bienvenida['explicacion'])
        self.layout.addWidget(self.explicacion)
        self.boton_iniciar = QPushButton("Iniciar Test")
        self.boton_iniciar.clicked.connect(self.mostrar_ventana_test)
        self.layout.addWidget(self.boton_iniciar)        
        self.setLayout(self.layout)
        
    def mostrar_ventana_test(self):
        self.ventana_test = VentanaTest()
        self.ventana_test.show()        
        self.close()
        