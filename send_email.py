

import smtplib
import time 

# Параметры подключения к серверу
smtp_server = "smtp.gmail.com"  # Адрес SMTP сервера
smtp_port = 587                   # Порт, использующийся для TLS/STARTTLS
sender_email = 'your mail'  # Адрес отправителя
receiver_email = 'receiver main'  # Адрес получателя
password = 'password'             # Пароль отправителя

# Текст сообщения
message = f"""\
Subject: Hi there
try:
tes_client
@ivan maslennikov {time.time()}"""

# Создание соединения с сервером и отправка сообщения
try:
    # Cоединение с сервером
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()  # Установка безопасного соединения
    server.login(sender_email, password)
    
    # Отправка сообщения

    server.sendmail(sender_email, receiver_email, message)

    
    print("Email successfully sent", time.time())
except Exception as e:
    print(f"Error: {e}")
finally:
    server.quit()
