import Adafruit_DHT
import tkinter as tk
from tkinter import Label
import time

# Configuración del sensor
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4  # Cambia el número de GPIO según tu conexión

# Crear ventana
root = tk.Tk()
root.title("Temperaturas por ELBARNY")
root.geometry("300x150")

# Etiqueta para mostrar temperatura
label_temp = Label(root, text="Temperatura: --- °C", font=("Arial", 14))
label_temp.pack(pady=20)

def actualizar_temperatura():
    """Función que actualiza la temperatura cada 2 segundos"""
    humedad, temperatura = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
    if temperatura is not None:
        label_temp.config(text=f" Temperatura: {temperatura:.2f}°C")
    else:
        label_temp.config(text="Error al leer el sensor")

    root.after(2000, actualizar_temperatura)  # Ejecutar nuevamente en 2 seg

# Iniciar actualización
actualizar_temperatura()

# Iniciar GUI
root.mainloop()