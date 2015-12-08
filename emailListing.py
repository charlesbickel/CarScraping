import smtplib
from email.mime.text import MIMEText

me = 'emailaddress'
you = 'emailaddress'

with open('carlisting.txt') as txt:
    msg = MIMEText(txt.read())
msg['Subject'] = 'Today\'s car listings'
msg['From'] = 'emailaddress'
msg['To'] = 'emailaddress'

conn = smtplib.SMTP('smtp.gmail.com', 587)
conn.ehlo()
conn.starttls()
conn.login('emailaddress', 'password')
conn.sendmail(me, you, msg.as_string())
conn.quit()