#connecting to env_variables for securing email credentials
import smtplib
import os
#to formating message
from email.message import EmailMessage
import json

env_email_address = os.environ.get('email_usr')
env_email_pass = os.environ.get('email_psswd')

msg_object = EmailMessage()
msg_object['Subject'] = 'testing automation'
msg_object['From'] = env_email_address
msg_object['To'] = 'cortezgonzalez74@gmail.com'
msg_object.set_content('Alert on a Domain')

#attachment
#with open('response.json().["WhoisRecord"]', 'r') as f:
    #json_file = f.read()
    #file_type = f.name
    #file_name = f.name

#msg_object.add_attachment(json_file, maintype='json', subtype=file_type, filename=file_name)

def email_sender():
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        # toidentify with mail server and encrypt
        smtp.login(env_email_address, env_email_pass)
        smtp.send_message(msg_object)





