import smtplib as SMTP
from email.message import EmailMessage
from dotenv import load_dotenv
import os

load_dotenv()

email_user = os.getenv("EMAIL_USER")
email_password = os.getenv("EMAIL_PASSWORD")

msg = EmailMessage()
msg["From"] = email_user
msg["To"] = "gustavopmorelli@gmail.com"
msg["Subject"] = "Teste de email"
msg.set_content("Corpo do teste de email")

with SMTP.SMTP("smtp.gmail.com", 587) as smtp:
  smtp.starttls()
  smtp.login(email_user, email_password)
  smtp.send_message(msg)