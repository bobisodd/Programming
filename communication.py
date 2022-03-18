import smtplib, ssl

port = 465 
password = input("Type your password and press enter: ")

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("my@gmail.com", password)

sender_email = "garrett_robert@student.mahoningctc.com"
receiver_email = "bgarrettjr19@gmail.com"
message = """\
Subject: Hi there

This message is sent from Python."""

server.sendmail(sender_email, receiver_email, message)
