#!/usr/bin/python

from gpiozero import MotionSensor
from picamera import PiCamera
from datetime import datetime
import time

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders

import os
from ConfigParser import SafeConfigParser

parser = SafeConfigParser()
parser.read('../myconfig/pc-mail.ini')

def mail(to, subject, text, attach):
   msg = MIMEMultipart()

   msg['From'] = gmail_user
   msg['To'] = to
   msg['Subject'] = subject

   msg.attach(MIMEText(text))

   part = MIMEBase('application', 'octet-stream')
   part.set_payload(open(attach, 'rb').read())
   Encoders.encode_base64(part)
   part.add_header('Content-Disposition',
           'attachment; filename="%s"' % os.path.basename(attach))
   msg.attach(part)

   mailServer = smtplib.SMTP("smtp.gmail.com", 587)
   mailServer.ehlo()
   mailServer.starttls()
   mailServer.ehlo()
   mailServer.login(gmail_user, gmail_pwd)
   mailServer.sendmail(gmail_user, to, msg.as_string())
   # Should be mailServer.quit(), but that crashes...
   mailServer.close()

camera = PiCamera()
pir = MotionSensor(4)

gmail_user = parser.get('GMAIL','user')
gmail_pwd = parser.get('GMAIL','password')
subject = parser.get('MAIL','subject')
message = parser.get('MAIL','message')

while True:
    pir.wait_for_motion()
    time.sleep(2)
    filename = datetime.now().strftime("./photo/%Y-%m-%d_%H.%M.%S.jpg")
    camera.capture(filename)
    mail(gmail_user, subject, message, filename)
    print(" emailing {} to {}  \n".format(filename,gmail_user))
    os.remove(filename)
    print(" deleting {} \n".format(filename))
    time.sleep(10)

