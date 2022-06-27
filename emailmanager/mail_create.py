import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.message import EmailMessage
from decouple import config

def send(receiver,subject,body,date):
    email_sender = config("email_sender")
    email_password = config("email_password")
    email_receiver = receiver
    smtp= smtplib.SMTP_SSL('smtp.gmail.com',465)
    smtp.login(email_sender, email_password)
    subject = subject
    body =  f' {body} bu mesaj {date} tarihinde Python tarafından gönderildi.'

    
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)
    context = ssl.create_default_context()


    smtp.sendmail(email_sender, email_receiver, em.as_string())




"""mail = smtplib.SMTP("smtp.gmail.com", 587)
mail.ehlo()
mail.starttls()



def sender(receiver, subject, text, date):

    print(receiver,subject,text,date)
    # gmail kullanıcı adımı ve şifremi giriyorum.
    mail.login("userrTest2021@gmail.com", "sbmcjtdlswfcmnsm2")
    mesaj = MIMEMultipart()


    mesaj["From"] = "userrTest2021@gmail.com"        # Gönderen kişi
    mesaj["To"] = receiver          # Alıcı

    mesaj["Subject"] = "Python Smtp ile Mail Gönderme"  # Konu

    body = text

    ###Python ile smtp ve email modülünü kullanarak mail gönderiyorum.

        

    body_text = MIMEText(body, "plain")
    mesaj.attach(body_text)
    
sender("salihturgay98@gmail.com","Python","Python 101", "27.06.2022")    
"""