import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile
from pydub import AudioSegment
import cycler
from scipy import signal
# Set the sampling rate and duration of the signals
sampling_rate = 44100
duration = 9

# Generate the time axis for the signals
noise = np.random.normal(0, 0.01, 132300)
noise2 = np.random.normal(0, 0.1, 132300)
time = np.linspace(0, duration, sampling_rate * duration, False)
time1 = np.linspace(0, 3, sampling_rate*3, False)
time2 = np.linspace(3, 6, sampling_rate*3, False)
time3 = np.linspace(6, 9, sampling_rate*3, False)

# Generate the signals
sine_wave = np.sin(2*np.pi*440*time)
sine_wave1 = np.sin(2*np.pi*440*time1)
sine_wave2 = np.sin(2*np.pi*440*time2)
sine_wave3 = np.sin(2*np.pi*440*time3)

bruit1 = sine_wave1+noise
bruit2 = sine_wave2+noise
bruit3 = sine_wave3+noise

bruit11 = sine_wave1+noise2
bruit22 = sine_wave2+noise2
bruit33 = sine_wave3+noise2


# Scale the signals to 16-bit integer range (-32768, 32767)
sine_wave *= 32767 / np.max(np.abs(sine_wave))
sine_wave1 *= 32767 / np.max(np.abs(sine_wave1))
sine_wave2 *= 32767 / np.max(np.abs(sine_wave2))
sine_wave3 *= 32767 / np.max(np.abs(sine_wave3))
bruit1 *= 32767 / np.max(np.abs(bruit1))
bruit2 *= 32767 / np.max(np.abs(bruit2))
bruit3 *= 32767 / np.max(np.abs(bruit3))
bruit11 *= 32767 / np.max(np.abs(bruit11))
bruit22 *= 32767 / np.max(np.abs(bruit22))
bruit33 *= 32767 / np.max(np.abs(bruit33))


# Convert the signals to 16-bit integers
sine_wave = sine_wave.astype(np.int16)
sine_wave1 = sine_wave1.astype(np.int16)
sine_wave2 = sine_wave2.astype(np.int16)
sine_wave3 = sine_wave3.astype(np.int16)

bruit1 = bruit1.astype(np.int16)
bruit2 = bruit2.astype(np.int16)
bruit3 = bruit3.astype(np.int16)
bruit11 = bruit11.astype(np.int16)
bruit22 = bruit22.astype(np.int16)
bruit33 = bruit33.astype(np.int16)

# Export the signals as WAV files
wavfile.write("Signals/Sin/sine_wave.wav", sampling_rate, sine_wave)
wavfile.write("Signals/Sin/sine_wave1.wav", sampling_rate, sine_wave1)
wavfile.write("Signals/Sin/sine_wave2.wav", sampling_rate, sine_wave2)
wavfile.write("Signals/Sin/sine_wave3.wav", sampling_rate, sine_wave3)

wavfile.write("Signals/Sin/sin_bruit1_001.wav", sampling_rate, bruit1)
wavfile.write("Signals/Sin/sin_bruit2_001.wav", sampling_rate, bruit2)
wavfile.write("Signals/Sin/sin_bruit3_001.wav", sampling_rate, bruit3)

wavfile.write("Signals/Sin/sin_bruit1_01.wav", sampling_rate, bruit11)
wavfile.write("Signals/Sin/sin_bruit2_01.wav", sampling_rate, bruit22)
wavfile.write("Signals/Sin/sin_bruit3_01.wav", sampling_rate, bruit33)

audio_file1 = AudioSegment.from_wav("Signals/Sin/sine_wave1.wav")

audio_file11 = AudioSegment.from_wav("Signals/Sin/sin_bruit1_01.wav")

# Convert the audio to a numpy array for plotting

audio_data1 = np.array(audio_file1.get_array_of_samples())
audio_data11 = np.array(audio_file11.get_array_of_samples())

# Compute the time array
time_array1 = np.arange(0, len(audio_data1)) / audio_file1.frame_rate
time_array11 = np.arange(0, len(audio_data11)) / audio_file11.frame_rate

# Plot the waveform
plt.plot(time_array1, audio_data1)
plt.plot(time_array11, audio_data11)
plt.xlim([0, 0.005])
plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.show()