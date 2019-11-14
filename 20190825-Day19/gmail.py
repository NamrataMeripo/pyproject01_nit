#!/usr/bin/python
import smtplib

gmail_user = 'dev.keshavkummari@gmail.com'
gmail_password = 'Python@12345'

from_1=gmail_user

to = ['keshav.kummari@gmail.com']

subject = 'Sending Email using GMAIL Mail Server-KeshavKummari'

body = 'Hi, \n  This is a Email Test \n Thanks, \nRoot.'

email_text = """\
From: %s
To: %s
Subject: %s

%s
""" % (from_1, ", ".join(to), subject, body)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 587)
    server.ehlo()
    server.login(gmail_user, gmail_password)
    server.sendmail(from_1, to, email_text)
    server.close()
    print ('Email has been sent!')
except:
    print ('Something went wrong...')
