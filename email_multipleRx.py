#***************************************************************************************************************
#                   This is a simple e-mail sending application for multiple recepient using python
#***************************************************************************************************************

#==========================================Imported module====================================================== 
import csv
import smtplib
from smtplib import SMTPException
#===============================================================================================================

sender = 'mayureshwaram8@gmail.com'

msg = "This is a test e-mail message."

try:
   smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
   smtpObj.starttls()  
   smtpObj.login("mayureshwaram8@gmail.com", "mayuram@04") 	# Authentication  
   
   filename = "email_records.csv"    						# csv file name
   
   with open(filename, 'r') as csvfile:    					# reading csv file  
       csvreader = csv.reader(csvfile) 						# creating a csv reader object  
       for row in csvreader:								# extracting each data row one by one
           print(row[2])
           if row[2]=="e-mail":
               continue
           smtpObj.sendmail(sender, row[2], msg)
       print ("Successfully sent email")
   
except SMTPException:
   print ("Error: unable to send email")
   
#===============================================================================================================

