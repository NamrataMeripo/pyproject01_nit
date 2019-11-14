
import smtplib

email = 'dev.keshavkummari@gmail.com'
password = 'Python@12345'

receiver = ['keshav.kummari@gmail.com','abhi.vennamaneni@gmail.com']

content = 'This is a Test Mail'

fromemail = email 

mail = smtplib.SMTP('smtp.gmail.com',587)
mail.ehlo()
mail.starttls()
mail.login(email,password)
mail.sendmail(fromemail,receiver,content)
