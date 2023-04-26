import numpy as np
from matplotlib import pyplot as plt
from pydub import AudioSegment
from scipy import signal
from scipy.io import wavfile
sampling_rate = 44100
import os.path
from os import path
t = np.linspace(0, 3, 132300, endpoint=False)


class Signal:
    def __init__(self, fichier1, fichier2, choix_filtre):
        self.fichier1 = fichier1
        self.fichier2 = fichier2
        self.choixFiltre = choix_filtre
        self.nom_fichier1 = self.fichier1.replace(".wav", "")
        self.nom_fichier2 = self.fichier2.replace(".wav", "")
        self.nom_fichier3 = self.nom_fichier2 + "_filtered" + str(self.choixFiltre)
        self.original, self.temps1 = generation_fonction_temps(fichier1)
        self.bruit, self.temps2 = generation_fonction_temps(fichier2)
        self.b, self.a = params_filtres(choix_filtre, self.fichier2)
        self.filtered = filtration_signal(self.b, self.a, self.bruit)
        self.filtered = self.filtered*2
        self.filtered = mise_en_forme_signal(self.filtered)
        sauvegarde_signal(self.nom_fichier3, self.filtered)


    def graph_builder(self,i, x, y, bruit):

        plt.figure(i)
        plt.plot(self.temps1, self.original)
        if bruit:
            plt.plot(self.temps2, self.bruit)
        plt.plot(self.temps2, self.filtered)
        plt.xlim(x)
        plt.ylim(y)
        plt.legend([self.nom_fichier1, self.nom_fichier2, self.nom_fichier3])
        plt.xlabel("Time (seconds)")
        plt.ylabel("Amplitude")
        plt.show(block=False)


def params_filtres(type, fichier):
    fichier_audio = AudioSegment.from_wav(fichier)

    if type == 1:
        low_cutoff = 350
        high_cutoff = 7500
        order = 4
        ny_quist_freq = 0.5 * fichier_audio.frame_rate
        low = low_cutoff / ny_quist_freq
        high = high_cutoff / ny_quist_freq
        b, a = signal.butter(order, [low, high], btype='bandpass')
        return b, a
    elif type == 2:
        cutoff = 500
        ny_quist_freq = 0.5 * (fichier_audio.frame_rate)
        high = cutoff / ny_quist_freq
        order = 10
        fs = 150.0
        b, a = signal.butter(order, high, btype='low')
        return b, a
    elif type == 3:
        cutoff_hz = 1000
        rp =1
        ny_quist_freq = 0.5 * (fichier_audio.frame_rate)
        Wn = cutoff_hz / ny_quist_freq
        order = 5
        b, a = signal.cheby1(order,rp, Wn, btype='lowpass')
        return b, a
    else:
        cutoff = 1000
        ny_quist_freq = 0.5 * (fichier_audio.frame_rate)
        high = cutoff / ny_quist_freq
        order = 10
        fs = 150.0
        b, a = signal.butter(order, high, btype='low')
        return b, a


def filtration_signal(b, a, fonction):
    filtered = signal.filtfilt(b, a, fonction)
    return filtered

'''def filtre1(fichier):
    fichier_audio = AudioSegment.from_wav(fichier)
    fonction = np.array(fichier_audio.get_array_of_samples())
    temps = np.arange(0, len(fonction)) / fichier_audio.frame_rate
    order = 10
    fs = 150.0
    cutoff = 4.0
    b, a = signal.butter(order, 5200, btype='low', fs=44100)
    filtered = signal.filtfilt(b, a, fonction)
    return filtered, temps
def filtre2(fichier):
    low_cutoff = 350
    high_cutoff = 7500
    order = 4
    fichier_audio = AudioSegment.from_wav(fichier)
    ny_quist_freq = 0.5*(fichier_audio.frame_rate)
    low = low_cutoff/ny_quist_freq
    high = high_cutoff/ny_quist_freq
    fonction = np.array(fichier_audio.get_array_of_samples())
    temps = np.arange(0, len(fonction)) / fichier_audio.frame_rate
    b, a = signal.butter(order, [low, high], btype='bandpass')
    filtered = signal.filtfilt(b, a, fonction)
    return filtered, temps'''

def mise_en_forme_signal(signal1):
    signal1 *= 32767 / np.max(np.abs(signal1))
    signal1 = signal1.astype(np.int16)
    return signal1


def generation_fonction_temps(file):
    fichier = AudioSegment.from_wav(file)
    fonction = np.array(fichier.get_array_of_samples())
    temps = np.arange(0, len(fonction)) / fichier.frame_rate
    return fonction, temps


def sauvegarde_signal(fichier, fonction):
    filtered = "Filtered"
    filtre = "Filtre"+fichier[-1]
    if "sin" in fichier:
        substring = 'Signals/Sin/'+filtered+'/'+filtre
        if not path.exists(substring):
            os.mkdir(substring)
        fichier = fichier.replace('Signals/Sin/', substring+'/')
    if "music" in fichier:
        substring = 'Signals/Music/' + filtered + '/'+filtre
        if not path.exists(substring):
            os.mkdir(substring)
        fichier = fichier.replace('Signals/Music/', substring+'/')
    if "voix" in fichier:
        substring = 'Signals/Voix/' + filtered + '/'+filtre
        if not path.exists(substring):
            os.mkdir(substring)
        fichier = fichier.replace('Signals/Voix/', substring+'/')
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
    i = 1
    audio_file1 = AudioSegment.from_wav("Signals/Sin/sine_wave1.wav")
    # Convert the audio to a numpy array for plotting
    audio_data1 = np.array(audio_file1.get_array_of_samples())
    # Compute the time array

    sin_butter_101 = Signal("Signals/Sin/sine_wave1.wav", "Signals/Sin/sin_bruit1_01.wav", 2)
    sin_butter_1001 = Signal("Signals/Sin/sine_wave1.wav", "Signals/Sin/sin_bruit1_001.wav", 1)
    sin_butter_201 = Signal("Signals/Sin/sine_wave2.wav", "Signals/Sin/sin_bruit2_01.wav", 1)
    sin_butter_2001 = Signal("Signals/Sin/sine_wave2.wav", "Signals/Sin/sin_bruit2_001.wav", 1)
    sin_butter_301 = Signal("Signals/Sin/sine_wave3.wav", "Signals/Sin/sin_bruit3_01.wav", 1)
    sin_butter_3001 = Signal("Signals/Sin/sine_wave3.wav", "Signals/Sin/sin_bruit3_001.wav", 1)
    music_butter_11 = Signal("Signals/Music/music1.wav", "Signals/Music/music1_bruit1.wav", 1)
    music_butter_12 = Signal("Signals/Music/music1.wav", "Signals/Music/music1_bruit2.wav", 1)
    voix_butter_1 = Signal("Signals/Voix/voix_3.wav", "Signals/Voix/voix1_bruit1.wav", 1)
    voix_butter_2 = Signal("Signals/Voix/voix_3.wav", "Signals/Voix/voix1_bruit2.wav", 1)
    ''' sin_butter_101.graph_builder(1)
    sin_butter_1001.graph_builder(2)
    sin_butter_201.graph_builder(3)
    sin_butter_2001.graph_builder(4)
    sin_butter_301.graph_builder(5)
    sin_butter_3001.graph_builder(6)
    music_butter_11.graph_builder(7)
    music_butter_12.graph_builder(8)'''
    voix_butter_1.graph_builder(9, [0.499, 0.501], [-400, 800], False)
    sin_butter_101.graph_builder(1, [0.490, 0.510], [-32000, 32000],True)
    plt.show()




    # Plot the waveform



main()