#***************************************************************************************************************
#                   This is a simple e-mail sending application using python
#***************************************************************************************************************

#==========================================Imported module====================================================== 
import smtplib
from smtplib import SMTPException
#===============================================================================================================

sender = 'mayureshwaram8@gmail.com'
receivers ='auti.mayur@yahoo.com'

msg = " This is a test e-mail message."

try:
   smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
   smtpObj.starttls()
    
   smtpObj.login("mayureshwaram8@gmail.com", "mayuram@04")     		# Authentication 
   smtpObj.sendmail(sender, receivers, msg)
   print ("Successfully sent email")
   
except SMTPException:
   print ("Error: unable to send email")
#===============================================================================================================
