import smtplib

gmail_user = 'sayed_eva@hotmail.com'
gmail_password = 'Sayed08sabeeha'

try:
    server = smtplib.SMTP_TLS('outlook.office365.com', 995)
    server.ehlo()
    server.login(gmail_user, gmail_password)
except:
    print ('Something went wrong...')
