import numpy as np
import wave
from subprocess import call



def generator(src, dst):

    
    wav_file = wave.open(dst, "w")
    ampWidth = 4
    sampleRate = 39000
    duration = 20
    nFrames = sampleRate * duration
    wav_file.setparams((2, ampWidth, sampleRate, nFrames, 'NONE', None))

    dataL = []
    dataR = []
    count = 0
    with open(src) as file:
        for i in file:
            if not count % 2:
                dataL.append(np.int32(i.rstrip()) << 14)
            else:
                dataR.append(np.int32(i.rstrip()) << 14)
            count = count + 1

    ns = np.column_stack((dataL, dataR)).ravel().astype(np.int32)
    wav_file.writeframes(ns.tobytes())

    wav_file.close()