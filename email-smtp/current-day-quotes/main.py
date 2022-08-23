import smtplib
import datetime as dt
from random import choice

MY_GMAIL = 'pass.Feiyan.3001@gmail.com'
GENERATED_PASSWORD = 'ldotnsajqiijozuf'

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 3:
    with open('quotes.txt', 'r') as data:
        quotes = data.read().splitlines()
        today_quote = choice(quotes)
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=MY_GMAIL, password=GENERATED_PASSWORD)
        connection.sendmail(
            from_addr=MY_GMAIL, 
            to_addrs='hoangtunguyen2002@gmail.com',
            msg=f'subject:Quote for today\n{today_quote}'
        )
