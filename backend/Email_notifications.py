import smtplib
from email.message import EmailMessage

from backend.EmailUsers import emailuser, emailpwd, receiver


def Email(message):
    gmailaddress = emailuser
    gmailpassword = emailpwd
    mailto = receiver

    msg = EmailMessage()
    msg["Subject"] = "WaterMed Connector notification"
    msg["From"] = gmailaddress
    msg["To"] = mailto
    msg.set_content(f"{message}")
    with smtplib.SMTP_SSL('smtp.gmail.com' , 465) as smtp:
        smtp.login(gmailaddress, gmailpassword)
        smtp.send_message(msg)
    print(f" \n Email Sent to {receiver}!")


