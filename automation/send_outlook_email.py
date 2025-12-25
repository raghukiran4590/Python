import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, recipient_email, subject, message):
    msg = MIMEMultipart('alternative')
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    text = 'This is a sample plain text'
    html = f'<html><body><h1>{message}</h1></body></html>'
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    msg.attach(part1)
    msg.attach(part2)

    smtp_server = 'smtp-mail.outlook.com'
    smtp_port = 587

    try:
        # create a secure SSL/TLS connection
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()

        # login to your outlook email
        server.login(sender_email, sender_password)
        
        #send email
        server.sendmail(send_email, recipient_email, msg.as_string())
        print('Email sent successfully')

    except smtplib.SMTPException as e:
        print('Error sending email ', str(e))
    
    finally:
        #close the connection
        server.quit()


sender_email = 'raghukiran@hotmail.com'
sender_password = 'TampaBay@123'
recipient_email = 'raghu.kiran@elevancehealth.com'
subject = 'Hello from Python Email'
message = 'This email was sent from Python API for Outlook'

send_email(sender_email, sender_password, recipient_email, subject, message)



