import datetime as dt
import pandas as pd
import random
import smtplib

# Obtener la fecha de hoy
now = dt.datetime.now()
today_month = now.month
today_day = now.day

# Leer el archivo CSV
df = pd.read_csv("birthdays.csv")

# Filtrar por mes y día
matching_birthdays = df[(df["month"] == today_month) & (df["day"] == today_day)]

# Verificar si hay coincidencias
if not matching_birthdays.empty:

    # Lista de plantillas de cartas disponibles
    letter_templates = ["letter_templates/letter_1.txt",
                        "letter_templates/letter_2.txt",
                        "letter_templates/letter_3.txt"]

    for _, row in matching_birthdays.iterrows():
        name = row["name"]
        email = row["email"]

        # Elegir aleatoriamente una carta
        letter_path = random.choice(letter_templates)

        # Leer el contenido de la carta y reemplazar [NAME]
        with open(letter_path, "r") as file:
            letter_content = file.read().replace("[NAME]", name)

        my_email = "hackthedayofficial@gmail.com"
        password = "ijsiuxkyoknlpduf"

        connection = smtplib.SMTP("smtp.gmail.com", 587)
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="diego.rdlvs1@gmail.com",
                            msg=f"Subject:Happy Birthday\n\n{letter_content}")
        connection.close()

        # Imprimir o guardar el mensaje personalizado
        print(letter_content)

else:
    pass





