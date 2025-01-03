import smtplib


my_email = "xxxxxxxx@gmail.com"
password = "abcd1234"

connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls()
connection.login(user= my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="xxxxxxxtest@yahoo.com", msg="Hello")
connection.close()







smtplib.SMTP("smtp.gmail.com", port=587)


