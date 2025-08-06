from dotenv import load_dotenv
load_dotenv()

import requests
import os
from twilio.rest import Client

api_key = '43b518eb2c6fc4073fc955d80b86134f'
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
lat_bucharest = 44.426765
long_bucharest = 26.102537



parameters={
    'lat': lat_bucharest,
    'lon': long_bucharest,
    'appid': api_key,
    'cnt': 4
}

response = requests.get('https://api.openweathermap.org/data/2.5/forecast', params=parameters)
response.raise_for_status()
weather_data = response.json()
# weather_data = response.json()['list'][0]['weather']
will_rain = False
for hour_data in weather_data['list']:
   condition_code = hour_data['weather'][0]['id']

   if int(condition_code) < 700:
       will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It`s going to rain today. Remember to bring your ☂️.",
        from_="+18585443785",
        to="+40723670508",
    )

    print(message.status)



