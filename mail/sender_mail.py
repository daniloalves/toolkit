# Import smtplib for the actual sending function
import smtplib, ssl

# Import the email modules we'll need
from email.mime.text import MIMEText

SMTP_USR  = "user"
SMTP_PWD  = "pass"
SMTP_HOST = "in-v3.mailjet.com"

FROM = "hacker@realmail.com"
TO   = "victim@mail.com"


msg = MIMEText('Tet body')

msg['Subject'] = 'Reset your credentials'
msg['From'] = "confidentFrom@mail.com" 
msg['To'] = TO

context = ssl.create_default_context()

with smtplib.SMTP_SSL(SMTP_HOST, 465, context=context) as server:
    server.login(SMTP_USR, SMTP_PWD)
    server.sendmail(FROM, [TO], msg.as_string())
    server.quit()

