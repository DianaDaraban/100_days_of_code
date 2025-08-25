#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

import requests
import os
from amadeus import Client, ResponseError, Location
from dotenv import load_dotenv
from twilio.rest import Client as TwilioClient


load_dotenv()


username_twilio = os.getenv('TWILIO_ACCOUNT_SID')
password_twilio = os.getenv('TWILIO_AUTH_TOKEN')

sheet_data = requests.get(url='https://api.sheety.co/cd82068654ddb2d88a38c602a9f952e2/flightDeals/prices').json()['prices']
print(sheet_data)

# amadeus_security_endpoint = 'https://test.api.amadeus.com/v1/security/oauth2/token'
# params = {
#     'grant_type': 'client_credentials',
#     'client_id': os.getenv('AMADEUS_API_KEY'),
#     'client_secret': os.getenv('AMADEUS_API_SECRET')
# }
#
# amadeus_auth = requests.post(url=amadeus_security_endpoint, data=params)
# access_token = amadeus_auth.json()['access_token']
#
#
# amadeus_checkin_endpoint = "https://test.api.amadeus.com/v2/reference-data/urls/checkin-links"
# checkin_params = {
#     "airline": "IB",
# }
#
# headers = {
#     "Authorization": f"Bearer {access_token}",
# }
#
# checkin_response = requests.get(url=amadeus_checkin_endpoint, headers=headers, params=params)
# print(checkin_response.json())



amadeus = Client(
    client_id= os.getenv('AMADEUS_API_KEY'),
    client_secret= os.getenv('AMADEUS_API_SECRET')
)



itineraries =[]
try:
    response = amadeus.shopping.flight_offers_search.get(
        originLocationCode='OTP',  # București Otopeni
        destinationLocationCode='BCN',  # Barcelona
        departureDate='2025-08-25',  # data dorită
        adults=1
    )
    # print(response.data)
    for data in response.data:
            itineraries = [flight for flight in data['itineraries'] if flight['segments'][0]['departure']['iataCode'] == 'OTP']
except ResponseError as error:
    print(error)

print(itineraries)

for item in itineraries:
    # params = {'keyword' : item['segments'][0]['arrival']['iataCode']}
    destination_iataCode = item['segments'][0]['arrival']['iataCode']
    print(destination_iataCode)
    # city = amadeus.reference_data.locations.get(keyword=f'{destination_iataCode}', subType=Location.AIRPORT)['address']['cityName']
    city = amadeus.reference_data.locations.get(keyword=f'{destination_iataCode}', subType=Location.AIRPORT)
    city_name = city.result['data'][0]['address']['cityName']
    print(city_name)
    # sheet_data = {
    #     'city': '',
    #     'iataCode': item['segments'][0]['arrival']['iataCode'],
    #     'lowestPrice': 54,
    #     'id': 2
    # }


# client = TwilioClient(username=username_twilio, password=password_twilio)
#
# client.messages.create(
#         body="This is a message!",
#         from_="+18585443785",
#         to="+40723670508",)