mport adafruit_dht
import board
import tkinter as tk
from tkinter import Label
import time

# Configuración del sensor
DHT_SENSOR = adafruit_dht.DHT22(board.D4)  # Cambia "D4" según el GPIO que uses

# Crear ventana
root = tk.Tk()
root.title("Temperaturas por ELBARNY")
root.geometry("300x150")

# Etiqueta para mostrar temperatura
label_temp = Label(root, text="Temperatura: --- °C", font=("Arial", 14))
label_temp.pack(pady=20)

def actualizar_temperatura():
    """Función que actualiza la temperatura cada 2 segundos"""
    try:
        temperatura = DHT_SENSOR.temperature
        if temperatura is not None:
            label_temp.config(text=f"Temperatura: {temperatura:.2f}°C")
        else:
            label_temp.config(text="Error al leer el sensor")
    except RuntimeError as error:
        label_temp.config(text="Error de lectura, intentando nuevamente...")

    root.after(2000, actualizar_temperatura)  # Ejecutar nuevamente en 2 seg

# Iniciar actualización
actualizar_temperatura()

# Iniciar GUI
root.mainloop()