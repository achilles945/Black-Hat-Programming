import smtplib
import time
# import win32com.client

smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_acct = 'senders_acc@gmail.com'
smtp_password = 'email_pass'
tgt_accts = ['recipient@gamil.com']

def plain_email(subject, contents):
    # form the message that incorporates the SMTP server data and messsage contents
    message = f'Subject: {subject}\nFrom {smtp_acct}\n'
    message += f'To: {tgt_accts}\n\n{contents}'
    server =smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    
    # connect and login to server with acc name and pass
    server.login(smtp_acct, smtp_password)

    #server.set_debuglevel(1)

    # invoke sendmail method with our account information, target acc, message
    server.sendmail(smtp_acct, tgt_accts, message)
    time.sleep(1)
    server.quit()


# windows specific function
'''
def outlook(subject, contents):
    outlook = win32com.client.Dispath("OutlookApplication")
    message = outlook.CreateItem(0)

    message.DeleteAfterSubmit = True
    message.Subject = subject
    message.Body = contents.decode()

    message.To = tgt_accts[0]
    message.Send()
'''
if __name__ == '__main__':
    plain_email('test2 message', 'attack at dawn.')
