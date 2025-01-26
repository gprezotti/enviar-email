import smtplib as SMTP
from email.message import EmailMessage
from dotenv import load_dotenv
import os

# Carrega as variáveis de ambiente
load_dotenv()

# Carrega as variáveis de ambiente em variáveis locais
email_user = os.getenv("EMAIL_USER")
email_password = os.getenv("EMAIL_PASSWORD")
email_recipient = os.getenv("EMAIL_RECIPIENT")
file = os.getenv("FILE_NAME")

msg = EmailMessage()
msg["From"] = email_user # Define o remetente do email
msg["To"] = email_recipient # Define o destinatário do email
msg["Subject"] = "Teste de email" # Define o assunto do email
msg.set_content("Corpo do teste de email") # Define o texto de corpo do email

# Abre o arquivo pdf e o insere como anexo no email
with open(file, "rb") as f:
  msg.add_attachment(f.read(), maintype='application', subtype='pdf', filename='arquivo.pdf')

# Envia o email pelo servidor smtp.gmail.com pela porta 587
with SMTP.SMTP("smtp.gmail.com", 587) as smtp:
  smtp.starttls() # Cripitografia TLS
  smtp.login(email_user, email_password) # Login no Gmail
  smtp.send_message(msg)