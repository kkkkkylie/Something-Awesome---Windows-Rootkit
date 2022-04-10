try: 
    import pyscreenshot
    from PIL import Image
    from SetUpDir import dir

except ModuleNotFoundError:
    from subprocess import call
    call("pip install " + ' ' + 'pyscreenshot', shell=True)

finally: 

    class ScreenShot:

        def __init__(self,dir):
            self.dir = dir

        def run(self):
            img = pyscreenshot.grab()
            img.save(self.dir + '\screenshot.png')
    
    