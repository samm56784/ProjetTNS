import numpy as np
from scipy.io import wavfile
from scipy import signal
# Set the sampling rate and duration of the signals
sampling_rate = 44100
duration = 9

# Generate the time axis for the signals
time = np.linspace(0, duration, sampling_rate * duration, False)
time1 = np.linspace(0, 3, sampling_rate*3, False)
time2 = np.linspace(3, 6, sampling_rate*3, False)
time3 = np.linspace(6, 9, sampling_rate*3, False)

# Generate the signals
sine_wave = np.sin(2*np.pi*440*time)
sine_wave1 = np.sin(2*np.pi*440*time1)
sine_wave2 = np.sin(2*np.pi*440*time2)
sine_wave3 = np.sin(2*np.pi*440*time3)
# Scale the signals to 16-bit integer range (-32768, 32767)
sine_wave *= 32767 / np.max(np.abs(sine_wave))
sine_wave1 *= 32767 / np.max(np.abs(sine_wave1))
sine_wave2 *= 32767 / np.max(np.abs(sine_wave2))
sine_wave3 *= 32767 / np.max(np.abs(sine_wave3))
# Convert the signals to 16-bit integers
sine_wave = sine_wave.astype(np.int16)
sine_wave1 = sine_wave1.astype(np.int16)
sine_wave2 = sine_wave2.astype(np.int16)
sine_wave3 = sine_wave3.astype(np.int16)

# Export the signals as WAV files
wavfile.write("Signals/sine_wave.wav", sampling_rate, sine_wave)
wavfile.write("Signals/sine_wave1.wav", sampling_rate, sine_wave1)
wavfile.write("Signals/sine_wave2.wav", sampling_rate, sine_wave2)
wavfile.write("Signals/sine_wave3.wav", sampling_rate, sine_wave3)
