import requests
import json

api = requests.get('http://api.openweathermap.org/data/2.5/forecast?lat=25,7272429&lon=-100,311263&appid=e552413b18a80652918bb9f1ddf10010&units=metric&lang=sp&cnt=1')
json_data = json.loads(api.content)

ciudad = json_data['city']['name']
descripcion = json_data['list']


#probabilidad de lluvia
for data in descripcion:
  propLluvia = data['pop']
  propLluvia = propLluvia * 100
  print(propLluvia)


for data in descripcion:    #sacar descripcion del clima
    print( data['weather'])
    clima = data['weather']
    for data2 in clima:
        descript = data2['description']

for data in descripcion:    #fecha y hora del pronostico
  fechaHora = data['dt_txt']
    


texto1 = f'Hoy en {ciudad} \nEl pronostico es el siguiente: {descript} \nTemperatura: °C \n{fechaHora}'

#Version actualizada para enviarse la informacion
requests.post('https://api.telegram.org/bot5585839781:AAE42khIUAXBDtyMP5E1WGgjGEMCUflQYhc/sendMessage', 
             data = { 'chat_id' : '1535633944', 'text' : texto1})


if propLluvia >= 60 and propLluvia <=80:
  texto2= f'Hay una probabilidad de {propLluvia}% que llueva, vaya preparado'
  requests.post('https://api.telegram.org/bot5585839781:AAE42khIUAXBDtyMP5E1WGgjGEMCUflQYhc/sendMessage', 
             data = { 'chat_id' : '1535633944', 'text' : texto2})
if propLluvia >= 80:
  texto3= f'Hay una probabilidad de {propLluvia}% que llueva, es muy seguro que llueva, preparese y vaya con precaución'
  requests.post('https://api.telegram.org/bot5585839781:AAE42khIUAXBDtyMP5E1WGgjGEMCUflQYhc/sendMessage', 
             data = { 'chat_id' : '1535633944', 'text' : texto3})
#\nTemp. Minima: {tempMin}°C \nTemp. Máx: {tempMax}
