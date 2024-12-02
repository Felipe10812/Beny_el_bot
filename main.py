# id chat: -1001677873072

# main.py
import requests
from config import WEATHERBIT_URL, TELEGRAM_URL, WEATHERBIT_TOKEN

# Coordenadas (Van a ser variables en el futuro)
LAT = 25.7263685
LON = -100.3119711

# Datos del clima desde Weatherbit
def obtener_clima_actual(lat, lon):
    url = f"{WEATHERBIT_URL}lat={lat}&lon={lon}&key={WEATHERBIT_TOKEN}"
    response = requests.get(url)
    print(response.json())  # Inspeccionar la respuesta
    return response.json()

# Envio de mensaje a Telegram
def enviar_mensaje(chat_id, texto):
    data = {
        'chat_id': chat_id,
        'text': texto
    }
    response = requests.post(TELEGRAM_URL, data=data)
    return response.json()

# Lógica principal
if __name__ == "__main__":
    chat_id = "-1001677873072"

    # Clima actual
    clima_actual = obtener_clima_actual(LAT, LON)
    data = clima_actual['data'][0] 
    ciudad = data['city_name']
    temp_actual = data['temp']
    feel = data['app_temp']
    viento = data['wind_spd']
    descripcion_actual = data['weather']['description']

    # Crear texto para Telegram
    texto = (
        f"Actualmente en {ciudad}:\n"
        f"Temperatura actual: {temp_actual} °C\n"
        f"Esta {descripcion_actual}\n"
        f"Sensación Térmica: {feel} °C\n"
        f"Viento: {viento} km/h"
    )

    # Enviar mensaje
    enviar_mensaje(chat_id, texto)