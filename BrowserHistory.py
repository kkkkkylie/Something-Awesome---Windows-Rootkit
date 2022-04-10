try: 
    import os
    import subprocess
    import browserhistory
except ModuleNotFoundError:
    from subprocess import call
    call("pip install " + ' ' + 'browswerhistory', shell=True)

class BrowserHistory:
    def __init__(self,dir):
        self.dir = dir
    def run(self):
        os.chdir(self.dir)
        browserhistory.write_browserhistory_csv()
