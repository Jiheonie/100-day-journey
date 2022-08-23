import smtplib

MY_GMAIL = 'pass.Feiyan.3001@gmail.com'
# password: GMAIL_PASSWORD = 'Feiyan_3001'
GENERATED_PASSWORD = 'ldotnsajqiijozuf'

MY_YAHOO = 'mymail.testing@yahoo.com'
YAHOO_PASSWORD = 'Feiyan_3001'


with smtplib.SMTP('smtp.gmail.com') as connection:
    connection.starttls()
    connection.login(user=MY_GMAIL, password=GENERATED_PASSWORD)
    connection.sendmail(from_addr=MY_GMAIL, to_addrs='hoangtunguyen2002@gmail.com',
                        msg='subject:Hello\nThis is the body of the email.')


import datetime as dt

now = dt.datetime.now()

date_of_birth = dt.datetime(year=2002, month=8, day=29, hour=4, minute=29, second=2)
print(date_of_birth)

print(type(now))