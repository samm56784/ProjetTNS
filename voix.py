import numpy as np
from scipy.io import wavfile
from scipy.io import wavfile
# Load the WAV file
sample_rate1, data1 = wavfile.read("Signals/Voix/voix_3.wav")
sample_rate2, data2 = wavfile.read("Signals/Voix/voix_6.wav")
sample_rate3, data3 = wavfile.read("Signals/Voix/voix_9.wav")
# Convert the data to a NumPy array
data1 = np.array(data1, dtype=float)
data2 = np.array(data2, dtype=float)
data3 = np.array(data3, dtype=float)

# Normalize the data to the range [-1, 1]
data1 /= np.max(np.abs(data1))
data2 /= np.max(np.abs(data2))
data3 /= np.max(np.abs(data3))
# Print the sample rate and shape of the data

noise = np.random.normal(0, 0.005, 144000)
noise2 = np.random.normal(0, 0.05, 144000)

bruit1 = data1 + noise
bruit2 = data2 + noise
bruit3 = data3 + noise
bruit11 = data1 + noise2
bruit22 = data2 + noise2
bruit33 = data3 + noise2

bruit1 *= 32767 / np.max(np.abs(bruit1))
bruit2 *= 32767 / np.max(np.abs(bruit2))
bruit3 *= 32767 / np.max(np.abs(bruit3))
bruit11 *= 32767 / np.max(np.abs(bruit11))
bruit22 *= 32767 / np.max(np.abs(bruit22))
bruit33 *= 32767 / np.max(np.abs(bruit33))
bruit1 = bruit1.astype(np.int16)
bruit2 = bruit2.astype(np.int16)
bruit3 = bruit3.astype(np.int16)
bruit11 = bruit11.astype(np.int16)
bruit22 = bruit22.astype(np.int16)
bruit33 = bruit33.astype(np.int16)

wavfile.write("Signals/Voix/voix1_bruit1.wav", 48000, bruit1)
wavfile.write("Signals/Voix/voix2_bruit1.wav", 48000, bruit2)
wavfile.write("Signals/Voix/voix3_bruit1.wav", 48000, bruit3)
wavfile.write("Signals/Voix/voix1_bruit2.wav", 48000, bruit11)
wavfile.write("Signals/Voix/voix2_bruit2.wav", 48000, bruit22)
wavfile.write("Signals/Voix/voix3_bruit2.wav", 48000, bruit33)

