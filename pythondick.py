import tkinter as tk
import random
import math

# --- CONFIGURACIÓN GLOBAL ---
# Velocidad de movimiento en píxeles por actualización
VELOCIDAD = 4    
# Milisegundos entre frames (menor número = más FPS/fluidez)
RETRASO = 15     
# Límite duro de ventanas para prevenir el congelamiento del sistema (RAM/CPU overflow)
MAX_VENTANAS = 50 

# Lista para rastrear objetos activos
ventanas_activas = []

class Perseguidor:
    """
    Clase que representa a una entidad perseguidora.
    Crea una ventana Toplevel de Tkinter independiente.
    """
    def __init__(self, root, x, y):
        """
        Inicializa la ventana y el dibujo.
        :param root: Ventana padre (Tk).
        :param x: Posición inicial X en pantalla.
        :param y: Posición inicial Y en pantalla.
        """
        self.window = tk.Toplevel(root)
        self.window.title("")
        
        # Configuración de la ventana: Sin bordes y siempre encima de otras ventanas
        self.window.overrideredirect(True)
        self.window.attributes('-topmost', True)
        
        # Intenta hacer el fondo transparente (Funciona principalmente en Windows)
        try:
            self.window.attributes('-transparentcolor', 'white')
        except Exception:
            print("Advertencia: La transparencia no es compatible con este SO.")
            
        # Dimensiones del personaje (Pequeño)
        self.width = 30
        self.height = 40
        
        # Posición flotante para cálculos precisos
        self.x = x
        self.y = y
        self.window.geometry(f"{self.width}x{self.height}+{int(self.x)}+{int(self.y)}")
        
        # Lienzo de dibujo
        self.canvas = tk.Canvas(self.window, width=self.width, height=self.height, bg='white', highlightthickness=0)
        self.canvas.pack()
        
        # --- DIBUJO DEL PERSONAJE ---
        color = "#ffb6c1" # Rosa claro
        # Tronco
        self.canvas.create_oval(8, 2, 22, 30, fill=color, outline=color)
        # Esferas inferiores
        self.canvas.create_oval(2, 25, 15, 38, fill=color, outline=color)
        self.canvas.create_oval(15, 25, 28, 38, fill=color, outline=color)
        
        # Control de duplicación
        self.spawn_cooldown = 0
        
        # Iniciar bucle de animación
        self.actualizar()

    def actualizar(self):
        """
        Calcula la nueva posición basada en la ubicación del mouse
        y maneja la lógica de duplicación.
        """
        try:
            # 1. Obtener coordenadas del mouse global
            mouse_x = self.window.winfo_pointerx()
            mouse_y = self.window.winfo_pointery()
            
            # 2. Calcular vector de dirección
            center_x = self.x + self.width/2
            center_y = self.y + self.height/2
            
            dx = mouse_x - center_x
            dy = mouse_y - center_y
            distancia = math.sqrt(dx**2 + dy**2)
            
            # 3. Mover si no ha alcanzado al mouse
            if distancia > 5:
                # Normalizar vector y aplicar velocidad
                move_x = (dx / distancia) * VELOCIDAD
                move_y = (dy / distancia) * VELOCIDAD
                
                # Efecto JITTER (Simular correr/vibrar)
                jitter = 2 
                move_x += random.uniform(-jitter, jitter)
                move_y += random.uniform(-jitter, jitter)
                
                # Actualizar posición
                self.x += move_x
                self.y += move_y
                
                self.window.geometry(f"+{int(self.x)}+{int(self.y)}")
            
            # 4. Lógica de Colisión (Duplicación)
            # Hitbox de 15 píxeles
            if distancia < 15 and self.spawn_cooldown == 0:
                if len(ventanas_activas) < MAX_VENTANAS:
                    # Crear nueva instancia desplazada aleatoriamente
                    offset_x = random.randint(-50, 50)
                    offset_y = random.randint(-50, 50)
                    nuevo = Perseguidor(root, self.x + offset_x, self.y + offset_y)
                    ventanas_activas.append(nuevo)
                    
                    # Evitar duplicación instantánea en cascada
                    self.spawn_cooldown = 40 
            
            # Reducir cooldown
            if self.spawn_cooldown > 0:
                self.spawn_cooldown -= 1

            # Programar siguiente frame
            self.window.after(RETRASO, self.actualizar)
            
        except Exception:
            # Manejo de errores si la ventana es destruida externamente
            pass

def cerrar_todo(event):
    """Función de emergencia para detener el script."""
    root.destroy()
    exit()

# --- BLOQUE PRINCIPAL ---
if __name__ == "__main__":
    # Configuración de la ventana raíz (invisible)
    root = tk.Tk()
    root.withdraw()

    # Obtener centro de pantalla
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    # Crear el primer perseguidor
    primero = Perseguidor(root, screen_width//2, screen_height//2)
    ventanas_activas.append(primero)

    # Bind de tecla de escape
    root.bind_all('<Escape>', cerrar_todo)
    
    # Iniciar bucle principal
    root.mainloop()
