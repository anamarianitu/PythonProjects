
# Birthday Wisher Starting Project #

import smtplib
import datetime as dt
import pandas
import random

MY_EMAIL = "plantasticnature@gmail.com"
PASSWORD = "anaaremere1234567890"

now = dt.datetime.now()
today_day = now.day
today_month = now.month
today = (today_month, today_day)

data = pandas.read_csv("birthdays.csv")

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}


if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=birthday_person["email"],
                                msg=f"Subject:Happy Birthday!\n\n{contents}"
                                )



