import adafruit_dht
import board
import tkinter as tk
from tkinter import Label
import time

# Configuración del sensor
DHT_SENSOR = adafruit_dht.DHT22(board.D4)  # Cambia "D4" según el GPIO que uses

# Crear ventana
root = tk.Tk()
root.title("Temperaturas por ELBARNY")
root.geometry("300x200")

# Etiquetas para mostrar información
label_temp = Label(root, text="Temperatura: --- °C", font=("Arial", 14))
label_temp.pack(pady=10)

label_contador = Label(root, text="Próxima actualización en: 2 seg", font=("Arial", 12))
label_contador.pack(pady=5)

def actualizar_temperatura(contador=2):
    """Función que actualiza la temperatura y muestra el tiempo restante"""
    try:
        temperatura = DHT_SENSOR.temperature
        if temperatura is not None:
            label_temp.config(text=f"Temperatura: {temperatura:.2f}°C")
        else:
            label_temp.config(text="Error al leer el sensor")
    except RuntimeError:
        label_temp.config(text="Error de lectura, intentando nuevamente...")

    # Reiniciar el contador
    label_contador.config(text=f"Próxima actualización en: {contador} seg")
    root.after(1000, actualizar_contador, contador - 1)  # Reducir contador cada segundo
    root.after(2000, actualizar_temperatura)  # Ejecutar nuevamente en 2 seg

def actualizar_contador(contador):
    """Actualiza el contador cada segundo"""
    if contador >= 0:
        label_contador.config(text=f"Próxima actualizacion en: {contador} seg")
        root.after(1000, actualizar_contador, contador - 1)

# Iniciar actualización y contador
actualizar_temperatura()

# Iniciar GUI
root.mainloop()