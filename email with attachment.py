#***************************************************************************************************************
#                   This is a e-mail(with attachment) sending application using python
#***************************************************************************************************************

#==========================================Imported module====================================================== 
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders
from smtplib import SMTPException
import os
#===============================================================================================================

USERNAME = "mayureshwaram8@gmail.com"
PASSWORD = "mayuram@04"

try:
    def sendMail(to, subject, text, files=[]):
        assert type(to)==list
        assert type(files)==list
        msg = MIMEMultipart()
        msg['From'] = USERNAME
        msg['To'] = COMMASPACE.join(to)
        msg['Date'] = formatdate(localtime=True)
        msg['Subject'] = subject
        msg.attach( MIMEText(text) )
        for file in files:
            part = MIMEBase('application', "octet-stream")
            part.set_payload( open(file,"rb").read() )
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename="%s"' %os.path.basename(file))
            msg.attach(part)
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo_or_helo_if_needed()
        server.starttls()
        server.ehlo_or_helo_if_needed()
        server.login(USERNAME,PASSWORD)
        server.sendmail(USERNAME, to, msg.as_string())
        server.quit()

    sendMail(["auti.mayur@yahoo.com"],"Test mail for attachment","Welcome Mayur",["/home/spanidea/Pictures/Mayur_pf.png",\
    "/home/spanidea/Downloads/GPIO_drvr_pi.pdf"])                                                                
    time.sleep(15)
    print ("Successfuly sent email")
    
except SMTPException:
   print ("Error: unable to send email")
#===============================================================================================================   
