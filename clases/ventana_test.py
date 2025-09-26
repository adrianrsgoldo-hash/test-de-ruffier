from PyQt5.QtWidgets import QLabel, QVBoxLayout, QPushButton, QLineEdit, QFormLayout, QHBoxLayout, QMessageBox
from PyQt5.QtCore import Qt, QTimer, QTime
from clases.ventana_base import VentanaBase
from clases.ventana_final import VentanaFinal
from recursos.instrucciones import instrucciones_test

class VentanaTest(VentanaBase):
    def __init__(self, titulo="Test de ruffier", ancho=1000, alto=800):
        super().__init__(titulo, ancho, alto)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_cronometro)
        self.time = None
        #layout principal
        self.layout_principal = QVBoxLayout()
        

        #widgets
        self.titulo = QLabel("Test de Ruffier")
        self.titulo.setObjectName("titulo")
        self.layout_principal.addWidget(self.titulo, alignment=Qt.AlignCenter)
    
        #nombre y edad
        self.nombre = QLabel('ingrese su nombre:')
        self.entrada_nombre = QLineEdit()
        self.entrada_nombre.setFixedWidth(200)
        self.edad = QLabel('ingrese su edad:')
        self.entrada_edad = QLineEdit()
        self.entrada_edad.setFixedWidth(80)
        self.layout_nombre_edad = QFormLayout()
        self.layout_nombre_edad.addRow(self.nombre, self.entrada_nombre)
        self.layout_nombre_edad.addRow(self.edad, self.entrada_edad)
        self.layout_principal.addLayout(self.layout_nombre_edad)
        
        #--Instrucciones y P0
        self.instruccion = QLabel(instrucciones_test['instruccion_P0'])
        
        self.cronometro_reposo = QPushButton("Cronómetro de 15 segundos de reposo")
        self.cronometro_reposo.setFixedWidth(300)
        self.cronometro_reposo.clicked.connect(lambda: self.cronometro_set(15))
        self.p0 = QLabel("Pulsaciones en reposo (P0):")
        self.entrada_p0 = QLineEdit()
        self.entrada_p0.setFixedWidth(100)
        self.layout_p0 = QFormLayout()
        self.layout_p0.addRow(self.p0, self.entrada_p0)
        
        self.layout_principal.addWidget(self.instruccion)
        self.layout_principal.addWidget(self.cronometro_reposo, alignment=Qt.AlignCenter)
        self.layout_principal.addLayout(self.layout_p0)
        
        #--Instrucciones y P1
        self.instruccion2 = QLabel(instrucciones_test['instruccion_P1'])
        
        self.cronometro = QLabel("--- Cronómetro ---")
        self.cronometro.setObjectName("cronometro")
        
        self.contador_sentadillas = QPushButton("Contador de sentadillas")
        self.contador_sentadillas.setFixedWidth(300)
        self.contador_sentadillas.clicked.connect(lambda: self.cronometro_set(45))
        self.cronometro_sentadillas = QPushButton("Cronómetro de 15 segundos Esfuerzo")
        self.cronometro_sentadillas.setFixedWidth(300)
        self.cronometro_sentadillas.clicked.connect(lambda: self.cronometro_set(15))
        self.p1 = QLabel("Pulsaciones después del esfuerzo (P1):")
        self.entrada_p1 = QLineEdit()
        self.entrada_p1.setFixedWidth(100)
        self.layout_p1 = QFormLayout()
        self.layout_p1.addRow(self.p1, self.entrada_p1)
        self.layout_horizontal = QHBoxLayout()
        self.layout_horizontal.addWidget(self.instruccion2)
        self.layout_horizontal.addWidget(self.cronometro, alignment=Qt.AlignRight)
        self.layout_principal.addLayout(self.layout_horizontal)
        self.layout_principal.addWidget(self.contador_sentadillas, alignment=Qt.AlignCenter)
        self.layout_principal.addWidget(self.cronometro_sentadillas, alignment=Qt.AlignCenter)
        self.layout_principal.addLayout(self.layout_p1)
        
        #--Instrucciones y P2
        self.instruccion3 = QLabel(instrucciones_test['instruccion_P2'])
        self.cronometro_1min = QPushButton("Cronómetro de 1 minuto descanso")
        self.cronometro_1min.setFixedWidth(300)
        self.cronometro_1min.clicked.connect(lambda: self.cronometro_set(59))
        self.instruccion4 = QLabel(instrucciones_test['instruccion_final'])
        self.cronometro_final = QPushButton("Cronómetro de 15 segundos recuperacion")
        self.cronometro_final.setFixedWidth(300)
        self.cronometro_final.clicked.connect(lambda: self.cronometro_set(15))
        self.p2 = QLabel("Pulsaciones después de un minuto (P2):")
        self.entrada_p2 = QLineEdit()
        self.entrada_p2.setFixedWidth(100)
        self.layout_p2 = QFormLayout()
        self.layout_p2.addRow(self.p2, self.entrada_p2)
        self.resultado = QPushButton("Ver resultado")
        self.resultado.setFixedWidth(200)
        self.resultado.clicked.connect(self.mostrar_ventana_final)
        self.layout_principal.addWidget(self.instruccion3)
        self.layout_principal.addWidget(self.cronometro_1min, alignment=Qt.AlignCenter)
        self.layout_principal.addWidget(self.instruccion4)
        self.layout_principal.addWidget(self.cronometro_final, alignment=Qt.AlignCenter)
        self.layout_principal.addLayout(self.layout_p2)
        self.layout_principal.addWidget(self.resultado, alignment=Qt.AlignCenter)
        
        self.setLayout(self.layout_principal)

    def cronometro_set(self, segundos):
        self.time = QTime(0, 0, segundos)
        self.cronometro.setText(self.time.toString("ss"))

        if self.timer.isActive():
            self.timer.stop()
    
        self.timer.start(1000)
        
    def update_cronometro(self):
        self.time = self.time.addSecs(-1)
        self.cronometro.setText(self.time.toString("ss"))
        if self.time == QTime(0, 0, 0):
            self.timer.stop()
            
    def mostrar_ventana_final(self):
        datos = self.validacion_datos()
        if datos:
            self.ventana_final = VentanaFinal(datos)
            self.ventana_final.show()        
            self.close()
            
    def validacion_datos(self):
        nombre = self.entrada_nombre.text().strip()
        edad = self.entrada_edad.text().strip()
        p0 = self.entrada_p0.text().strip()
        p1 = self.entrada_p1.text().strip()
        p2 = self.entrada_p2.text().strip()
        
        if not nombre:
            self.mostrar_mensaje("Por favor, ingrese su nombre.")
            return None
        if not edad.isdigit():
            self.mostrar_mensaje("Por favor, ingrese una edad válida.")
            return None
        if int(edad) < 7:
            self.mostrar_mensaje("La edad mínima para realizar el test es 7 años.")
            return None
        for i, valor in zip(['P0', 'P1', 'P2'], [p0, p1, p2]):
            if not valor.isdigit():
                self.mostrar_mensaje(f"Por favor, ingrese un valor numérico válido para {i}.")
                return None
            if int(valor) <= 0:
                self.mostrar_mensaje(f"Por favor, ingrese un valor positivo para {i}.")
                return None
        return {
            "nombre": nombre,
            "edad": int(edad),
            "p0": int(p0),
            "p1": int(p1),
            "p2": int(p2)
        }
        
    def mostrar_mensaje(self, mensaje):
        QMessageBox.warning(self, "Error", mensaje)
        