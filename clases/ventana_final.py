from PyQt5.QtWidgets import QLabel, QVBoxLayout, QPushButton
from clases.ventana_base import VentanaBase

class VentanaFinal(VentanaBase):
    def __init__(self, datos):
        super().__init__(titulo="Resultado del Test", ancho=600, alto=400)
        self.datos = datos
        self.indice = (4*((self.datos["p0"])+(self.datos["p1"])+(self.datos["p2"]))-200)/10
        txt_res1 = "bajo. ¡Acuda al médico de inmediato!"
        txt_res2 = "satisfactorio. ¡Vea a su médico!"
        txt_res3 = "promedio. Puede valer la pena ver a su médico para que lo revise."
        txt_res4 = "por encima del promedio"
        txt_res5 = "alto"
        self.layout = QVBoxLayout()
        #widget
        self.indice_label = QLabel(f"Aquí se mostrará el índice de Ruffier: {self.indice}")
        if self.datos['edad'] >= 15:
            if self.indice >= 15:
                self.interpretacion = txt_res1
            elif self.indice >= 11 and self.indice <= 14.9:
                self.interpretacion = txt_res2
            elif self.indice >= 6 and self.indice <= 10.9:
                self.interpretacion = txt_res3
            elif self.indice >= 0.5 and self.indice <= 5.9:
                self.interpretacion = txt_res4
            else:
                self.interpretacion = txt_res5
        elif self.datos['edad'] >= 13 and self.datos['edad'] <= 14:
            if self.indice >= 16.5:
                self.interpretacion = txt_res1
            elif self.indice >= 12.5 and self.indice <= 16.4:
                self.interpretacion = txt_res2
            elif self.indice >= 7.5 and self.indice <= 12.4:
                self.interpretacion = txt_res3
            elif self.indice >= 2 and self.indice <= 7.4:
                self.interpretacion = txt_res4
            else:
                self.interpretacion = txt_res5
        elif self.datos['edad'] >= 11 and self.datos['edad'] <= 12:
            if self.indice >= 18:
                self.interpretacion = txt_res1
            elif self.indice >= 14 and self.indice <= 17.9:
                self.interpretacion = txt_res2
            elif self.indice >= 9 and self.indice <= 13.9:
                self.interpretacion = txt_res3
            elif self.indice >= 3.5 and self.indice <= 8.9:
                self.interpretacion = txt_res4
            else:
                self.interpretacion = txt_res5
        elif self.datos['edad'] >= 9 and self.datos['edad'] <= 10:
            if self.indice >= 19.5:
                self.interpretacion = txt_res1
            elif self.indice >= 15.5 and self.indice <= 19.4:
                self.interpretacion = txt_res2
            elif self.indice >= 10.5 and self.indice <= 15.4:
                self.interpretacion = txt_res3
            elif self.indice >= 5 and self.indice <= 10.4:
                self.interpretacion = txt_res4
            else:
                self.interpretacion = txt_res5
        elif self.datos['edad'] >= 7 and self.datos['edad'] <= 8:
            if self.indice >= 21:
                self.interpretacion = txt_res1
            elif self.indice >= 17 and self.indice <= 20.9:
                self.interpretacion = txt_res2
            elif self.indice >= 12 and self.indice <= 16.9:
                self.interpretacion = txt_res3
            elif self.indice >= 6.5 and self.indice <= 11.9:
                self.interpretacion = txt_res4
            else:
                self.interpretacion = txt_res5
                
        self.interpretacion_label = QLabel(self.interpretacion)
        self.volver_boton = QPushButton("Volver al inicio")
        self.volver_boton.clicked.connect(self.reiniciar)
        self.layout.addWidget(self.indice_label)
        self.layout.addWidget(self.interpretacion_label)
        self.layout.addWidget(self.volver_boton)
        self.setLayout(self.layout)
        
    def reiniciar(self):
        from clases.ventana_bienvenida import VentanaBienvenida
        self.ventana_bienvenida = VentanaBienvenida()
        self.ventana_bienvenida.show()        
        self.close()
            
    
        