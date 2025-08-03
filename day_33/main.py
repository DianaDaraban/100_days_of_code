import requests
from datetime import datetime
import smtplib
import time

email = 'disu.lut@gmail.com'
password = 'mbonyhqualziuahj'

response = requests.get(url='http://api.open-notify.org/iss-now.json')
response.raise_for_status()

data = response.json()

MY_LAT = 44.426765
MY_LNG = 26.102537

parameters = {
    'lat': MY_LAT,
    'lng': MY_LNG,
    'formatted':0
}

response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()
sunrise_data = response.json()

iss_latitude = float(data['iss_position']['latitude'])
iss_longitude = float(data['iss_position']['longitude'])
sunrise = int(sunrise_data['results']['sunrise'].split('T')[1].split(':')[0])
sunset = int(sunrise_data['results']['sunset'].split('T')[1].split(':')[0])

time_hour = datetime.now().hour

while True:
    time.sleep(60)
    if  MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LNG +5 <= iss_longitude <= MY_LNG+5 and sunset < time_hour < sunrise:
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(from_addr=email, to_addrs=email, msg='Subject: Look at the sky!\n\nLook at the sky, you can see the ISS!')

    else:
        print('It is not visible')


