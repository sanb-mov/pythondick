# pythondick

Un script divertido y ligero escrito en Python usando `tkinter`. Genera pequeñas figuras animadas que persiguen incansablemente el cursor del mouse por toda la pantalla.

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)

## 🕹️ ¿Cómo funciona?

Al ejecutar el script:
1. Aparece una **pequeña figura** en el centro de la pantalla.
2. La figura **persigue tu mouse** con un efecto de animación de "correr" (vibración/jitter).
3. **Mecánica de Infección:** Si dejas que la figura toque el puntero del mouse, ¡aparecerá otra!
4. El proceso se repite hasta alcanzar el límite de seguridad establecido.

> **Nota:** Las figuras son ventanas independientes sin bordes (`overrideredirect`) que se mantienen siempre visibles (`topmost`).

## ⚠️ Advertencia y Seguridad

Este script se comporta visualmente como un "virus de broma" (similar a los antiguos *desktop pranks*), pero es totalmente inofensivo.

*   **Kill Switch (Botón de Pánico):** Si la pantalla se llena demasiado, presiona la tecla **`ESC` (Escape)** para cerrar todo el programa inmediatamente.
*   **Límite de Seguridad:** El código tiene un límite predeterminado (`MAX_VENTANAS = 50`) para evitar que tu computadora se quede sin memoria RAM (Fork Bomb protection).

## 🚀 Instalación y Uso

### Prerrequisitos
*   Tener **Python 3** instalado.
*   No requiere librerías externas (usa `tkinter`, `random` y `math` que vienen con Python).

### Ejecutar

1. Clona el repositorio o descarga el archivo `pythondick.py`.
2. Abre una terminal en la carpeta.
3. Ejecuta:

```bash
python chaser_prank.py
