# Python code to illustrate Sending mail with attachments 
# from your Gmail account 
# email with attachment using python and google app code
# libraries to be imported 
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

import tkinter as tk
from tkinter import filedialog

from pathlib import Path

import getpass

fromaddr = "gokulyc@gmail.com"
toaddr = "gokulyc@kindle.com"

# instance of MIMEMultipart 
msg = MIMEMultipart() 

# storing the senders email address 
msg['From'] = fromaddr 

# storing the receivers email address 
msg['To'] = toaddr 

# storing the subject 
msg['Subject'] = "convert book file"

# string to store the body of the mail 
body = "hi, PFA"

# attach the body with the msg instance 
msg.attach(MIMEText(body, 'plain')) 



# open the file to be sent 

root = tk.Tk()
root.withdraw()

file_path = Path(filedialog.askopenfilename())

filename = file_path.name
attachment = open(file_path, "rb") 

# instance of MIMEBase and named as p 
p = MIMEBase('application', 'octet-stream') 

# To change the payload into encoded form 
p.set_payload((attachment).read()) 

# encode into base64 
encoders.encode_base64(p) 

p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 

# attach the instance 'p' to instance 'msg' 
msg.attach(p) 

# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 

# start TLS for security 
s.starttls() 

# Authentication
# google app password  or password
s.login(fromaddr, "") 

# Converts the Multipart msg into a string 
text = msg.as_string() 

# sending the mail 
s.sendmail(fromaddr, toaddr, text) 

# terminating the session 
s.quit() 