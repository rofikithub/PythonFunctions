import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# http://mcqtarget.com/cpanel
smtp_server = 'mcqtarget.com'
smtp_port   = 587
username    = '_mainaccount@mcqtarget.com'
password    = '9HCqDOVfkdR4'
sender      = "mcqtkzns@mcqtarget.com"


receivers = ['rofik.it.bd@gmail.com', 'rofik.info.bd@gmail.com']


subject = 'Test Email'
body = """\
<html>
  <body>
    <p>Hi,<br>
    This is a <b>test</b> email without an attachment sent using <a href="https://www.python.org">Python</a>.</p>
  </body>
</html>
"""


message = MIMEMultipart()
message['From'] = sender
message['Subject'] = subject
message.attach(MIMEText(body, 'plain'))

try:
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(username, password)
    
    for reciver in receivers:
        message['To'] = reciver
        text = message.as_string()
        server.sendmail(sender, reciver, text)
        print(f'Email sent to {reciver}')
    

    server.quit()
    
    print('All emails sent successfully.')
except Exception as e:
    print(f'Failed to send email: {str(e)}')
