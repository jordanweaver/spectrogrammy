"""
spectrogrammy is an art utility that creates pretty stuff out of
your favorite song
"""

import os
import wave
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

def graph_spectogram(wav_file):
    """A spectrogram, or sonogram, is a visual representation of the spectrum
    of frequencies in a sound.  Horizontal axis represents time, Vertical axis
    represents frequency, and color represents amplitude.
    """

    size = (19, 12)     # inches
    dots = 300          # dpi

    sound_array, frame_rate = get_wave_info(wav_file)
    plt.figure(num=None, figsize=size, dpi=dots)
    plt.title('specgram of {}'.format(wav_file))
    pss, freqs, t = mlab.specgram(sound_array, Fs=frame_rate)

    ext = [0, t.max() / 10000, 0, freqs.max() / 1000]
    log_pss = np.log(pss)
    plt.imshow(log_pss, origin='lower', cmap='jet', aspect='auto', extent=ext)
    plt.savefig('spectrogram.png')

def get_wave_info(wav_file):

    wav = wave.open(wav_file, 'r')
    frames = wav.readframes(-1)
    frame_rate = wav.getframerate()
    sound_array = np.fromstring(frames, dtype=np.int16)

    wav.close()

    return sound_array, frame_rate

if __name__ == '__main__':
    audir = 'test_audio'
    filename = 'difference_frequency_2_tone_stimulus.wav'
    wav_file = os.path.join(audir, filename)

    graph_spectogram(wav_file)
