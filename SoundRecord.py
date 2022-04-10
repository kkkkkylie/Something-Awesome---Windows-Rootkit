try:
    import sounddevice as sd
    import numpy as np
    import soundfile as sf
    import scipy.io.wavfile as wav
    
except ModuleNotFoundError:
    from subprocess import call

    call("pip install " + ' ' + 'wav', shell=True)
    call("pip install " + ' ' + 'numpy', shell=True)
    call("pip install " + ' ' + 'soundfile', shell=True)
    call("pip install " + ' ' + 'sounddevice', shell=True)


class SoundRecord: 

    def __init__(self, duration, dir):
        self.frequency=44100
        self.duration = duration  
        self.dir = dir

    def run(self): 
        record = sd.rec(int(self.duration) * self.frequency, samplerate=self.frequency, channels=2)
        sd.wait()
        sf.write(self.dir + "\sound_record.wav", record, self.frequency)
        # print("Record file stored")
