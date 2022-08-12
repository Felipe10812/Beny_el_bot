import requests
import json

api = requests.get('http://api.openweathermap.org/data/2.5/forecast?lat=25,7272429&lon=-100,311263&appid=e552413b18a80652918bb9f1ddf10010&units=metric&lang=sp&cnt=1')
json_data = json.loads(api.content)

ciudad = json_data['city']['name']
descripcion = json_data['list']

for data in descripcion:
	print( data['weather'])
	clima = data['weather']
	for data2 in clima:
		descript = data2['description']

	


texto = f'Hoy en {ciudad} \nEl pronostico es el siguiente: {descript}'

#Version actualizada para enviarse la informacion
requests.post('https://api.telegram.org/bot5585839781:AAE42khIUAXBDtyMP5E1WGgjGEMCUflQYhc/sendMessage', 
             data = { 'chat_id' : '-1001677873072', 'text' : texto})	
