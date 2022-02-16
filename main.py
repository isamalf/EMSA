import os
import smtplib
import imghdr
from email.message import EmailMessage

import yfinance as yf
import datetime as dt
import pandas as pd
from pandas_datareader import data as pdr
import time

EMAIL_ADDRESS = os.environ.get('ialfuqahaTest@gmail.com')
EMAIL_PASSWORD = os.environ.get('qhlkscjrwbedhhqq')

msg = EmailMessage()

yf.pdr_override()
start =dt.datetime(2022,2,15)
now = dt.datetime.now()

stock="QQQ"
TargetPrice=350

msg['Subject'] = 'Alert on '+ stock+'!'
msg['From'] = 'ialfuqahaTest@gmail.com'
msg['To'] = 'isamalfuqaha@gmail.com'

alerted=False

while 1:

    df = pdr.get_data_yahoo(stock, start, now)
    currentClose=df["Adj Close"][-1]

    condition=currentClose>TargetPrice

    if(condition and alerted==False):

        alerted=True

        message=stock +" Has activated the alert price of "+ str(TargetPrice) +\
         "\nCurrent Price: "+ str(currentClose)

        print(message)
        msg.set_content(message)


        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login("ialfuqahaTest@gmail.com", "qhlkscjrwbedhhqq")
            smtp.send_message(msg)

            print("completed")
    else:
        print("No new alerts")
    time.sleep(60)