from twilio.rest import Client
import requests
import os
from dotenv import load_dotenv
load_dotenv()

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
stock_parameters = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK,
    'apikey': os.getenv("API_KEY_STOCK"),
    'outputsize': 'compact'
}
response = requests.get('https://www.alphavantage.co/query', params=stock_parameters)
data = response.json()['Time Series (Daily)']
stock_data = list(data.values())[:2]
stock_date = list(data.keys())[:2][1]
news_parameters = {
    'q': COMPANY_NAME,
    'from':stock_date,
    'sortBy': 'popularity',
    'apiKey': os.getenv('API_KEY_NEWS')
}
news_response = requests.get('https://newsapi.org/v2/everything',  params=news_parameters)
news_data = news_response.json()['articles'][:3]
yesterday_stock = float(stock_data[0]['4. close'])
day_before_stock = float(stock_data[1]['4. close'])
diff_percentage = abs((yesterday_stock - day_before_stock) / day_before_stock) * 100
percentage = round(((yesterday_stock - day_before_stock) / day_before_stock) * 100, 1)

if percentage > 0:
    percentage_text = '🔺'+ str(percentage) + '%'
elif percentage == 0:
    percentage_text = '🔸'+ str(percentage)+ '%'
else:
    percentage_text = '🔻' + str(percentage)+ '%'

if diff_percentage >= 5:
    client = Client(account_sid, auth_token)
    for news in news_data:
        message = client.messages.create(
            body=f"{STOCK}: {percentage_text}\nHeadline: {news['title']}\nBrief: {news['description']}",
            from_="+18585443785",
            to="+40723670508",
        )
        print(message.status)
else:
    print("No News")