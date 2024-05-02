from email.message import EmailMessage
from password2 import password
import ssl
import smtplib

email_sender = 'paddylltoi1967@gmail.com'
email_password = password
email_receiver = 'gillgracie88@gmail.com'

subject = "Boo Yaaa Bitches"
body = """
Just sent you an email from my Python3 programme.
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)


context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
