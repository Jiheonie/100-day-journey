##################### Extra Hard Starting Project ######################
import pandas
from datetime import datetime
from random import randint
import smtplib


MY_GMAIL = 'pass.Feiyan.3001@gmail.com'
GENERATED_PASSWORD = 'ldotnsajqiijozuf'


# 1. Update the birthdays.csv
data = pandas.read_csv('birthdays.csv')
birhtday_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}


# 2. Check if today matches a birthday in the birthdays.csv
today = datetime.now()
today_tuple = (today.month, today.day)


# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if today_tuple in birhtday_dict:
    file_path = f'letter_templates/letter_{randint(1,3)}.txt'
    birthday_person = birhtday_dict[today_tuple]
    with open(file_path, 'r') as letter:
        data = letter.read()
        new_letter = data.replace('[NAME]', birthday_person['name'])

    # 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=MY_GMAIL, password=GENERATED_PASSWORD)
        connection.sendmail(
            from_addr=MY_GMAIL,
            to_addrs=MY_GMAIL,
            msg=f'subject:Happy birthday\n{new_letter}'
        )
