# Email Sending

This is a simple project that automates email sending using Python, leveraging the 
`smtplib` library to connect to an SMTP server (such as Gmail) and send messages with 
attachments or simple content.


## HOW TO RUN THE PROJECT ##

1. Clone the repository:
git clone https://github.com/gprezotti/enviar-email.git

2. Install the dependencies:
pip install -r requirements.txt

3. Create the `.env` file to store your email credentials securely:
EMAIL_USER=example@example.com
EMAIL_PASSWORD=your_password_or_token
EMAIL_RECIPIENT=example@example.com
FILE_NAME=file.extension

4. Run the `bot.py` script:
python bot.py


## LIBRARIES USED ##

- `smtplib`: Standard library for email sending.
- `email.message`: To create email messages.
- `python-dotenv`: To load environment variables from the `.env` file.


## LICENSE ##

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for more 
details.