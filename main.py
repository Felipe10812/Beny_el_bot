# id chat: -1001677873072

import requests
import json

apiActual = requests.get('https://api.openweathermap.org/data/2.5/weather?lat=25,7263685&lon=-100,3119711&appid=e552413b18a80652918bb9f1ddf10010&units=metric&lang=sp&cnt=2')
json_actual = json.loads(apiActual.content)

apiPronostico = requests.get('http://api.openweathermap.org/data/2.5/forecast?lat=25,7272429&lon=-100,311263&appid=e552413b18a80652918bb9f1ddf10010&units=metric&lang=sp&cnt=1')
json_pron = json.loads(apiPronostico.content)


tempActual = json_actual['main']['temp']
feel = json_actual['main']['feels_like']
viento =json_actual['wind']['speed']
description = json_actual['weather']

for item in description:
  desc = item['description']
  

ciudad = json_pron['city']['name']
descripcion = json_pron['list']


for datamain in descripcion:
  temp= datamain['main']['temp']
  tempMax = datamain['main']['temp_max']
  tempMin = datamain['main']['temp_min']
  sensacion = datamain['main']['feels_like']

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
    

texto1 = f'Actualmente en {ciudad}: \nTemp. Actual: {tempActual} °C. \nEsta {desc}\nSensación Térmica de: {feel}°C \nViento: {viento} km/h'
texto2 = f'Pronostico {fechaHora} en \n{ciudad} \n\nEl pronostico es el siguiente: {descript} \nTemperatura: {temp} °C \nTemp. Minima: {tempMin}°C \nTemp. Máx: {tempMax} \nSensación térmica de: {sensacion}°C '

requests.post('https://api.telegram.org/bot5585839781:AAE42khIUAXBDtyMP5E1WGgjGEMCUflQYhc/sendMessage', 
             data = { 'chat_id' : '-1001677873072', 'text' : texto1})

#Version actualizada para enviarse la informacion
requests.post('https://api.telegram.org/bot5585839781:AAE42khIUAXBDtyMP5E1WGgjGEMCUflQYhc/sendMessage', 
             data = { 'chat_id' : '-1001677873072', 'text' : texto2})


if propLluvia >= 60 and propLluvia <=80:
  texto3= f'Hay una probabilidad de {propLluvia}% que llueva, vaya preparado'
  requests.post('https://api.telegram.org/bot5585839781:AAE42khIUAXBDtyMP5E1WGgjGEMCUflQYhc/sendMessage', 
             data = { 'chat_id' : '--1001677873072', 'text' : texto3})
if propLluvia > 80:
  texto4= f'Hay una probabilidad de {propLluvia}% que llueva, es muy seguro que llueva, preparese y vaya con precaución'
  requests.post('https://api.telegram.org/bot5585839781:AAE42khIUAXBDtyMP5E1WGgjGEMCUflQYhc/sendMessage', 
             data = { 'chat_id' : '-1001677873072', 'text' : texto4})
