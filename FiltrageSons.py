import numpy as np
from matplotlib import pyplot as plt
from pydub import AudioSegment
from scipy import signal
from scipy.io import wavfile
sampling_rate = 44100
t = np.linspace(0, 3, 132300, endpoint=False)


class Signal:
    def __init__(self, fichier1,fichier2):
        self.fichier1 = fichier1
        self.fichier2 = fichier2
        self.nom_fichier1 = self.fichier1.replace(".wav", "")
        self.nom_fichier2 = self.fichier2.replace(".wav", "")
        self.nom_fichier3 = self.nom_fichier2 + "_filtered"
        self.original, self.temps1 = generation_fonction_temps(fichier1)
        self.bruit, self.temps2 = generation_fonction_temps(fichier2)
        self.filtered, self.temps3 = filtre1(self.fichier2)
        self.filtered = mise_en_forme_signal(self.filtered)
        sauvegarde_signal(self.nom_fichier3, self.filtered)


    def graph_builder(self):
        plt.figure()
        plt.plot(self.temps1, self.original)
        plt.plot(self.temps2, self.bruit)
        plt.plot(self.temps3, self.filtered)
        plt.xlim([0, 0.005])
        plt.legend([self.nom_fichier1, self.nom_fichier2, self.nom_fichier3])
        plt.xlabel("Time (seconds)")
        plt.ylabel("Amplitude")
        plt.show(block=False)








def filtre1(fichier):
    fichier_audio = AudioSegment.from_wav(fichier)
    fonction = np.array(fichier_audio.get_array_of_samples())
    temps = np.arange(0, len(fonction)) / fichier_audio.frame_rate
    order = 5
    fs = 50.0
    cutoff = 1.0
    b, a = signal.butter(order, cutoff / (fs / 2), btype='low')
    filtered = signal.filtfilt(b, a, fonction)
    return filtered, temps


def mise_en_forme_signal(signal1):
    #signal1 *= 32767 / np.max(np.abs(signal1))
    signal1 = signal1.astype(np.int16)
    return signal1


def generation_fonction_temps(file):
    fichier = AudioSegment.from_wav(file)
    fonction = np.array(fichier.get_array_of_samples())
    temps = np.arange(0, len(fonction)) / fichier.frame_rate
    return fonction, temps


def sauvegarde_signal(fichier, fonction):
    if ".wav" in fichier:
        wavfile.write(fichier, sampling_rate, fonction)
    else:
        fichier = fichier+".wav"
        wavfile.write(fichier, sampling_rate, fonction)




'''def graph_builder(temps1,temps2,temps3,fonction_originale,fonction_bruitée,fonction_retablie,nom1,nom2,nom3):
    plt.figure()
    plt.plot(temps1, fonction_originale)
    plt.plot(temps2, fonction_bruitée)
    plt.plot(temps3, fonction_retablie)
    plt.xlim([0, 0.005])
    plt.legend([nom1, nom2, nom3])
    plt.xlabel("Time (seconds)")
    plt.ylabel("Amplitude")'''


def main():

    audio_file1 = AudioSegment.from_wav("Signals/Sin/sine_wave1.wav")
    # Convert the audio to a numpy array for plotting
    audio_data1 = np.array(audio_file1.get_array_of_samples())
    # Compute the time array

    sin_butter_101 = Signal("Signals/Sin/sine_wave1.wav", "Signals/Sin/sin_bruit1_01.wav")
    sin_butter_1001 = Signal("Signals/Sin/sine_wave1.wav", "Signals/Sin/sin_bruit1_001.wav")
    sin_butter_201 = Signal("Signals/Sin/sine_wave2.wav", "Signals/Sin/sin_bruit2_01.wav")
    sin_butter_2001 = Signal("Signals/Sin/sine_wave2.wav", "Signals/Sin/sin_bruit2_001.wav")
    sin_butter_301 = Signal("Signals/Sin/sine_wave3.wav", "Signals/Sin/sin_bruit3_01.wav")
    sin_butter_3001 = Signal("Signals/Sin/sine_wave3.wav", "Signals/Sin/sin_bruit3_001.wav")
    sin_butter_101.graph_builder()
    sin_butter_1001.graph_builder()
    sin_butter_201.graph_builder()
    sin_butter_2001.graph_builder()
    
    plt.show()




    # Plot the waveform



main()