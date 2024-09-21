import datetime as dt
import random
import pandas
import smtplib

my_mail = "deneme@gmail.com"
my_password = "deneme"

now = dt.datetime.now()
today_month = now.month
today_day = now.day
today = (today_month, today_day)

birthday_data = pandas.read_csv("birthdays.csv")

#important
birthday_dict = {(data_row["month"], data_row["date"]): data_row for (index, data_row) in birthday_data.iterrows()}

print(birthday_dict)

if (today_month, today_day) in birthday_dict:

      with open(f"letter_templates/letter_{random.randint(1, 3)}.txt", "r") as f:
         birthday_person = birthday_dict[(today_month, today_day)]
         content = f.read()
         new_content = content.replace("[NAME]", birthday_person["name"])

      with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
         connection.starttls()
         connection.login(my_mail, my_password)
         connection.sendmail(from_addr=my_mail,to_addrs=birthday_person["mail"], msg=f"Subject: Happy Birthday, {new_content}")
         print(new_content)






