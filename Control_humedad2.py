import adafruit_dht
import board
import tkinter as tk
from tkinter import Label
import time

# Configuración del sensor
DHT_SENSOR = adafruit_dht.DHT22(board.D4)  # Cambia "D4" según el GPIO que uses

# Crear ventana
root = tk.Tk()
root.title("Temperatura y Humedad por ELBARNY")
root.geometry("300x250")

# Etiquetas para mostrar información
label_temp = Label(root, text="Temperatura: --- °C", font=("Arial", 14))
label_temp.pack(pady=10)

label_humedad = Label(root, text="Humedad: --- %", font=("Arial", 14))
label_humedad.pack(pady=10)

label_contador = Label(root, text="Próxima actualización en: 2 seg", font=("Arial", 12))
label_contador.pack(pady=5)

def actualizar_temperatura_humedad(contador=2):
    """Actualiza temperatura y humedad"""
    try:
        temperatura = DHT_SENSOR.temperature
        humedad = DHT_SENSOR.humidity
        
        if temperatura is not None and humedad is not None:
            label_temp.config(text=f"Temperatura: {temperatura:.2f}°C")
            label_humedad.config(text=f"Humedad: {humedad:.2f}%")
        else:
            label_temp.config(text="Error al leer el sensor")
            label_humedad.config(text="Error al leer la humedad")
    except RuntimeError:
        label_temp.config(text="Error de lectura, intentando nuevamente...")
        label_humedad.config(text="Error de lectura, intentando nuevamente...")

    label_contador.config(text=f"Próxima actualización en: {contador} seg")
    root.after(1000, actualizar_contador, contador - 1)
    root.after(2000, actualizar_temperatura_humedad)

def actualizar_contador(contador):
    """Actualiza el contador cada segundo"""
    if contador >= 0:
        label_contador.config(text=f"Próxima actualización en: {contador} seg")
        root.after(1000, actualizar_contador, contador - 1)

# Iniciar actualización con humedad incluida
actualizar_temperatura_humedad()

# Iniciar GUI
root.mainloop()