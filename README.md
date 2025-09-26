# Test de Ruffier

Esta aplicación, desarrollada en Python con PyQt5, permite realizar el **Test de Ruffier**, una prueba sencilla para evaluar la capacidad de recuperación del corazón tras el ejercicio. El usuario sigue instrucciones guiadas, introduce sus datos y obtiene una interpretación automática de su condición física.

## Estructura del Proyecto

- **main.py**  
  Punto de entrada de la aplicación. Inicializa la interfaz y aplica los estilos.

- **clases/**
  - **ventana_base.py**  
    Clase base para las ventanas, maneja el centrado y tamaño.
  - **ventana_bienvenida.py**  
    Ventana inicial con instrucciones y botón para iniciar el test.
  - **ventana_test.py**  
    Ventana principal del test: recoge datos, muestra instrucciones, cronómetros y validaciones.
  - **ventana_final.py**  
    Muestra el resultado del índice de Ruffier y su interpretación según la edad.

- **recursos/**
  - **instrucciones.py**  
    Diccionario con textos de instrucciones para cada etapa del test.

- **estilos/**
  - **estilos.qss**  
    Archivo de estilos para la interfaz gráfica (colores, fuentes, botones, etc).

## Funcionamiento

1. **Bienvenida:**  
   El usuario ve una introducción y explicación del test.

2. **Ingreso de datos:**  
   Se solicita nombre y edad.

3. **Test guiado:**  
   El usuario sigue los pasos:
   - Medición de pulso en reposo (P0) con cronómetro.
   - Realización de sentadillas con contador y cronómetro.
   - Medición de pulso tras el esfuerzo (P1) y tras un minuto de recuperación (P2).

4. **Resultados:**  
   Se calcula el índice de Ruffier y se muestra una interpretación personalizada según la edad.

## Ejecución

Asegúrate de tener PyQt5 instalado. Ejecuta:

```
python main.py
```

## Créditos

Desarrollado por [Tu Nombre].  
Basado en el protocolo del Test de Ruffier.