# import smtplib
#
# my_email = 'disu.lut@gmail.com'
# password = 'mbonyhqualziuahj'
# with smtplib.SMTP('smtp.gmail.com') as connection:
#     # Secure email
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs='di_lut@yahoo.com', msg='Subject:Hello, test!\n\n This is body of my email.')

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# day_of_the_week = now.weekday()
# print(day_of_the_week)
#
# date_of_birth = dt.datetime(year=1986, month=3, day=12, hour=13, minute=30)
# print(date_of_birth)

import datetime as dt
import json
import smtplib
import random

current_day_of_week = dt.datetime.now().weekday()

with open('quotes.txt', 'r') as data_file:
    data = data_file.readlines()
random_quote = random.choice(data)

email = 'disu.lut@gmail.com'
password = 'mbonyhqualziuahj'

with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(user=email, password=password)
    if current_day_of_week == 4:
        connection.sendmail(from_addr=email, to_addrs='di_lut@yahoo.com', msg=f'Subject:Friday Quote!\n\n{random_quote}')



