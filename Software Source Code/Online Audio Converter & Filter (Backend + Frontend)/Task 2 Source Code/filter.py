from scipy.signal import butter, lfilter

import wave
import numpy as np

# source code from
# https://stackoverflow.com/questions/12093594/how-to-implement-band-pass-butterworth-filter-with-scipy-signal-butter





def butter_bandpass(lowcut, highcut, fs, order=5):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return b, a


def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

def filter_func(src, low, high):
    fs = 5000.0
    lowcut = low
    highcut = high

    wr = wave.open(src, 'r')
    # Set the parameters for the output file.
    param = list(wr.getparams())



    ww = wave.open('filtered.wav', 'w')
    ww.setparams(param)

    data = np.frombuffer(wr.readframes(wr.getnframes()), dtype=np.int32)
    
    left, right = data[0::2], data[1::2]



    nl = butter_bandpass_filter(left, lowcut, highcut, fs)
    nr = butter_bandpass_filter(right, lowcut, highcut, fs)
    ns = np.column_stack((nl, nr)).ravel().astype(np.int32)

    ww.writeframes(ns.tobytes())
    wr.close()
    ww.close()
