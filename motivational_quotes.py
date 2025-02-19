import smtplib
import datetime as dt
import random


now = dt.datetime.now()
year = now.year
month = now.month
day = now.day
day_of_week = now.weekday()
date_of_birth = dt.datetime(year=year, month=month, day=day)

if day_of_week == 0:
    print("Is monday! Here its your weekly motivational quote Diego\n")

    # Leer el archivo de texto línea por línea
    with open("quotes.txt", "r", encoding="utf-8") as file:
        quotes = file.readlines()

    # Limpiar espacios en blanco y comillas
    quotes = [quote.strip() for quote in quotes if quote.strip()]

    # Seleccionar una cita aleatoria
    random_quote = (random.choice(quotes))

    my_email = "hackthedayofficial@gmail.com"
    password = "ijsiuxkyoknlpduf"


    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(from_addr=my_email,
                        to_addrs="diego.rdlvs1@gmail.com",
                        msg=f"Subject:Motivational Monday Quote\n\n{random_quote}")
    connection.close()
else:
    pass




