import numpy as np
from matplotlib import pyplot as plt
from pydub import AudioSegment
from scipy import signal
from scipy.io import wavfile

sampling_rate = 44100
order = 5
fs = 50.0
cutoff = 1.0
b, a = signal.butter(order, cutoff / (fs / 2), btype='low')


audio_file1 = AudioSegment.from_wav("Signals/Sin/sine_wave1.wav")

audio_file11 = AudioSegment.from_wav("Signals/Sin/sin_bruit1_01.wav")

# Convert the audio to a numpy array for plotting

audio_data1 = np.array(audio_file1.get_array_of_samples())
audio_data11 = np.array(audio_file11.get_array_of_samples())
t = np.linspace(0, 3, 132300, endpoint=False)

# Compute the time array
time_array1 = np.arange(0, len(audio_data1)) / audio_file1.frame_rate
time_array11 = np.arange(0, len(audio_data11)) / audio_file11.frame_rate

filtered = signal.filtfilt(b, a, audio_data11)
filtered_ajusted_gain = filtered*1.35

# Plot the waveform
plt.plot(time_array1, audio_data1)
plt.plot(time_array11, audio_data11)
plt.plot(t,filtered)
plt.plot(t,filtered_ajusted_gain)
plt.xlim([0, 0.005])
plt.legend(['Sin original','Sin bruité','Sin bruité puis filtré','Sin bruité puis filtré(gain ajusté)'])

plt.xlabel("Time (seconds)")
plt.ylabel("Amplitude")
plt.show()

filtered *= 32767 / np.max(np.abs(filtered))
filtered = filtered.astype(np.int16)
wavfile.write("Signals/Sin/sine_wave_filtered.wav", sampling_rate, filtered)


