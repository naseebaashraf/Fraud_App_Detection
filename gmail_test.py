# Python code for Sending mail from
# your Gmail account
import smtplib

def send_mail(subject,message,to):

    # creates SMTP session
    s = smtplib.SMTP('smtp.gmail.com', 587)

    # start TLS for security
    s.starttls()

    # Authentication
    gmail_id = 'fraudappdetection2021@gmail.com'
    gmail_password = 'mainproject2021'
    s.login(gmail_id, gmail_password)

    # message to be sent
    message = 'Subject: {}\n\n{}'.format(subject, message)

    # sending the mail
    s.sendmail(gmail_id, to, message)

    print(to, message)

    # terminating the session
    s.quit()

#send_mail("heoo","hai",'kites.sarath@gmail.com')