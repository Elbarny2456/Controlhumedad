import Adafruit_DHT
import time

# Configuración del sensor 
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4  # Cambia según el pin que uses

def abrir_algo():
    """Función que abre la llave por un tiempo y luego la cierra n"""
    print("🔓 Voy a abrir la llave we...")
    time.sleep(10)  # Esperar 10 segundos antes de cerrar(cambiar dependiendo del tiempo que se necesite)
    print("🔒 Cerrando la llave...")

try:
    while True:
        humedad, temperatura = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        
        if humedad is not None:
            print(f"💧 Humedad: {humedad:.2f}% | 🌡 Temperatura: {temperatura:.2f}°C")

            if humedad < 70:  # Cambia el umbral según necesites
                abrir_algo()
        else:
            print("Error al leer el sensor. Reintentando...")
        
        time.sleep(3600)  # Esperar 1 hora antes de la próxima lectura
except KeyboardInterrupt: #ctrl+c pa apagarlo
    print("\nPrograma detenido manualmente. ¡Hasta luego!")