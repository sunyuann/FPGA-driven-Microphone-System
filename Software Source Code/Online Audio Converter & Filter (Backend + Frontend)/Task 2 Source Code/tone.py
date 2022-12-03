import wave
import numpy as np

# source code from
# https://stackoverflow.com/questions/43963982/python-change-pitch-of-wav-file



def frequency(src, fre):
    wr = wave.open(src, 'r')
    # Set the parameters for the output file.
    par = list(wr.getparams())
    par = tuple(par)
    ww = wave.open('pitch.wav', 'w')
    ww.setparams(par)

    fr = 40
    sz = wr.getframerate()//fr  # Read and process 1/fr second at a time.
    # A larger number for fr means less reverb.
    c = int(wr.getnframes()/sz)  # count of the whole file
    shift = fre//fr  # shifting 100 Hz
    for num in range(c):
        da = np.frombuffer(wr.readframes(sz), dtype=np.int32)
        left, right = da[0::2], da[1::2]  # left and right channel
        lf, rf = np.fft.rfft(left), np.fft.rfft(right)
        lf, rf = np.roll(lf, shift), np.roll(rf, shift)
        if shift > 0:
            lf[0:shift], rf[0:shift] = 0, 0
        else:
            lf[shift:-1], rf[shift:-1] = 0, 0
        nl, nr = np.fft.irfft(lf), np.fft.irfft(rf)
        ns = np.column_stack((nl, nr)).ravel().astype(np.int32)
        ww.writeframes(ns.tobytes())
    wr.close()
    ww.close()