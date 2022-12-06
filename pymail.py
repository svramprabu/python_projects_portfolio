from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'svramprabu@gmail.com'
email_password = 'enter your password here'

email_receiver = input("Please enter the receiver mail id: ")#'wahati1747@edinel.com'
subject =input("Enter the subject: ") #"Don't forget to reply"
body =input("Type the body of the mail: ") #"""Trying to send a mail using python"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body) 

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())

