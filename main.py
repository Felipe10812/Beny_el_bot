import requests
import json

api = requests.get('http://api.openweathermap.org/data/2.5/forecast?lat=25,7272429&lon=-100,311263&appid=e552413b18a80652918bb9f1ddf10010&units=metric&lang=sp&cnt=1')
json_data = json.loads(api.content)

def tiempoCiudades(ciudad):
	ciudad = json_data['city']
	descripcion = json_data['list']
	estadoCielo = '' 
	temperatura = ''
	city = 'San Nicolás de los Garza'
	
	for data in descripcion:
		nombre = ciudad['name']
		if nombre == city:
			estadoCielo = descripcion['weather.description']
			temperatura = data['temp_max']['temp_min']


	text = f'Prediccion de hoy en {ciudad} \nCielo {estadoCielo} temperatura {temperatura}'
	print(f"Prediccion de hoy en { ciudad['name'] } \n Cielo: {estadoCielo} \n Temperatura: {temperatura}")
	return textoFinal

#tiempo = tiempoCiudades('description')


requests.post('https://api.telegram.org/bot5585839781:AAE42khIUAXBDtyMP5E1WGgjGEMCUflQYhc/sendMessage', 
              data = { 'username': '@Felipe_108', 'text':'tiempo' })
	