import numpy as np
from scipy import signal, io
import matplotlib.pyplot as plt

# Generate noisy signal
t = np.linspace(0, 9, 396900, endpoint=False)
y = np.sin(2 * np.pi * 10 * t) + 0.5 * np.random.normal(size=396900)

# Apply a low-pass filter
b, a = signal.butter(4, 0.1, 'low')
y_filt = signal.filtfilt(b, a, y)

io.wavfile.write('Signals/noisy_signal.wav', 44100, np.int16(y / np.max(np.abs(y)) * 32767))
io.wavfile.write('Signals/filtered_signal.wav', 44100, np.int16(y_filt / np.max(np.abs(y_filt)) * 32767))
# Plot the original and filtered signals
plt.plot(t, y, label='Noisy signal')
plt.plot(t, y_filt, label='Filtered signal')
plt.legend()
plt.show()
