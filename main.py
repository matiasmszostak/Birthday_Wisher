import smtplib
import datetime as dt
import random

my_email = "appdetesting@gmail.com"
password = "shpp phzt dahr vhif"

smtplib.SMTP("smtp.gmail.com", port=587)

quotes = []

with open ("quotes.txt", "r") as file:
    for line in file:
        quote = line.strip()
        quotes.append(quote)
print(quotes)



now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()

print(f"Day of the week: {day_of_week}")

if day_of_week == 6:
    random_quote = random.choice(quotes)
    print(random_quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="appdetesting@yahoo.com",
                            msg=f"Subject:The quote of the week\n\n {random_quote}.")











