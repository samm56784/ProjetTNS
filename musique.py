from pydub import AudioSegment
from pydub.generators import Sine, WhiteNoise
import numpy as np
from scipy.io import wavfile
# create a 1-second segment with a sine wave of 440 Hz
sine_wave = Sine(440).to_audio_segment(duration=2000)
noise = np.random.normal(0, 0.01, 132300)
noise2 = np.random.normal(0, 0.1, 132300)
# create a 4-second sequence with ascending notes
notes = [400,100,440,200,300,494,587, 554, 600,400,100,440,200,300,494,587, 554, 600]
notes1 = [400, 100, 440, 200, 300, 494]
notes2 = [587, 554, 600, 400, 100, 440]
notes3 = [200, 300, 494, 587, 554, 600]


def match_target_amplitude(sound, target_dBFS):
    change_in_dBFS = target_dBFS - sound.dBFS
    return sound.apply_gain(change_in_dBFS)


sequence = sum([Sine(n).to_audio_segment(duration=500) for n in notes])
sequence1 = sum([Sine(n).to_audio_segment(duration=500) for n in notes1])
sequence2 = sum([Sine(n).to_audio_segment(duration=500) for n in notes2])
sequence3 = sum([Sine(n).to_audio_segment(duration=500) for n in notes3])


bruit = WhiteNoise().to_audio_segment(duration=3000)
bruit1 = match_target_amplitude(bruit, -40.0)
bruit2 = match_target_amplitude(bruit, -20.0)

# concatenate the sine wave and the sequence
music = sequence
music1 = sequence1.overlay(bruit1)
music2 = sequence2.overlay(bruit1)
music3 = sequence3.overlay(bruit1)
music11 = sequence1.overlay(bruit2)
music22 = sequence2.overlay(bruit2)
music33 = sequence3.overlay(bruit2)


# export the music to a WAV file
sequence.export("Signals/music.wav", format="wav", bitrate="16", parameters=["-ar", "44100"])
sequence1.export("Signals/Music/music1.wav", format="wav", bitrate="16", parameters=["-ar", "44100"])
sequence2.export("Signals/Music/music2.wav", format="wav", bitrate="16", parameters=["-ar", "44100"])
sequence3.export("Signals/Music/music3.wav", format="wav", bitrate="16", parameters=["-ar", "44100"])

music1.export("Signals/Music/music1_bruit1.wav", format="wav", bitrate="16", parameters=["-ar", "44100"])
music2.export("Signals/Music/music2_bruit1.wav", format="wav", bitrate="16", parameters=["-ar", "44100"])
music3.export("Signals/Music/music3_bruit1.wav", format="wav", bitrate="16", parameters=["-ar", "44100"])

music11.export("Signals/Music/music1_bruit2.wav", format="wav", bitrate="16", parameters=["-ar", "44100"])
music22.export("Signals/Music/music2_bruit2.wav", format="wav", bitrate="16", parameters=["-ar", "44100"])
music33.export("Signals/Music/music3_bruit2.wav", format="wav", bitrate="16", parameters=["-ar", "44100"])
