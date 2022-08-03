# https://api.telegram.org/
# https://core.telegram.org/bot/api
# https://api.openweathermap.org/data/2.5/forecast?lat=25,7272429&lon=-100,311263&appid=e552413b18a80652918bb9f1ddf10010&units=metric&lang=sp&cnt=3
# Importaciones 
import requests
import json

api = requests.get('https://api.openweathermap.org/data/2.5/forecast?lat=25,7272429&lon=-100,311263&appid=e552413b18a80652918bb9f1ddf10010&units=metric&lang=sp&cnt=3')
json_data = json.loads(api.content)

def timpoCiudades(ciudad):
	ciudad = json_data["city"]
	estadoCielo = '' 
	temperatura = ''

	for ciudadData in ciudad:
		if ciudadData['name'] == ciudad:
			estadoCielo = ciudadData['description']
			temperatura = ciudadData['temp_max']['temp_min']
	
	textoFinal = f'Prediccion de hoy en {ciudad} \nCielo {estadoCielo} temperatura {temperatura}'

	return textoFinal

timpo = timpoCiudades('San Nicolás de los Garza')

requests.post('https://api.telegram.org/bot5585839781:AAE42khIUAXBDtyMP5E1WGgjGEMCUflQYhc/getMe', 
	      data = { 'chat_id': '@probandolo', 'text':'timpo' })

