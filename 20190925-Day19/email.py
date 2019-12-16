
#!/usr/bin/python
import smtplib

gmail_user = 'm.namrata05@gmail.com'
password = 'Namrata@1983'

from_1 = gmail_user
to : ['namrata.meripo@gmail.com']
subject : 'sending hello note'
body : ' Hi How are you?'


email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (from_1, ", ".join(to), subject, body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 587)
    server.ehlo()
    server.login(gmail_user, password)
    server.sendmail(from_1, to, email_text)
    server.close()
    print ('Email has been sent!')
except:
    print ('Something went wrong...')
