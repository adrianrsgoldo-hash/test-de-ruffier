from PyQt5.QtWidgets import QLabel, QVBoxLayout, QPushButton
from clases.ventana_base import VentanaBase

class VentanaBienvenida(VentanaBase):
    def __init__(self):
        super().__init__(titulo="Bienvenida", ancho=600, alto=500)
        self.layout = QVBoxLayout()
        #widget
        self.label_bienvenida = QLabel("¡Bienvenido a la Aplicación de control de salud!")
        self.layout.addWidget(self.label_bienvenida)
        self.explicacion = QLabel(
        """El Test de Ruffier es una prueba sencilla que permite valorar la capacidad de recuperación del corazón.

        Procedimiento:
        - Permanecer en reposo durante 5 minutos.
        - Medir el pulso en reposo durante 15 segundos (P0).
        - Realizar 30 sentadillas en 45 segundos.
        - Medir el pulso inmediatamente después del esfuerzo (P1).
        - Un minuto después, medir nuevamente el pulso (P2).

        Con estas mediciones se calcula el Índice de Ruffier, que indica la condición física:
        - Índice bajo → buena condición física.
        - Índice alto → fatiga rápida y baja tolerancia al esfuerzo.
        """
        )
        self.layout.addWidget(self.explicacion)
        self.boton_iniciar = QPushButton("Iniciar Test")
        self.layout.addWidget(self.boton_iniciar)        
        self.setLayout(self.layout)