##################### Extra Hard Starting Project ######################
import datetime as dt
import random

import pandas
import smtplib

from day_29.password_manager.generator import letters

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

now = dt.datetime.now()
today = now.day
month=now.month

email = 'disu.lut@gmail.com'
password = 'mbonyhqualziuahj'

data = pandas.read_csv('birthdays.csv')
data_dict = data.to_dict(orient='records')
letters = []


with open('letter_templates/letter_1.txt', 'r') as letter1:
    letters.append(letter1.read())
with open('letter_templates/letter_2.txt', 'r') as letter2:
    letters.append(letter2.read())
with open('letter_templates/letter_3.txt', 'r') as letter3:
    letters.append(letter3.read())

index = random.randint(0,len(letters)-1)

for person in data_dict:
    if person['month'] == month and person['day'] == today:
        with smtplib.SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(from_addr=email, to_addrs='di_lut@yahoo.com', msg=f'Subject: Happy birhtday {person['name']}!\n\n{letters[index].replace('[NAME]',person['name'])}')

