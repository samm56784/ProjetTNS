from pydub import AudioSegment
from pydub.generators import Sine

# create a 1-second segment with a sine wave of 440 Hz
sine_wave = Sine(440).to_audio_segment(duration=2000)

# create a 4-second sequence with ascending notes
notes = [400,100,440,200,300,494,587, 554, 600,400,100,440,200,300,494,587, 554, 600]
notes1 = [400,100,440,200,300,494]
notes2 = [587, 554, 600,400,100,440]
notes3 = [200,300,494,587, 554, 600]
sequence = sum([Sine(n).to_audio_segment(duration=500) for n in notes])
sequence1 = sum([Sine(n).to_audio_segment(duration=500) for n in notes1])
sequence2 = sum([Sine(n).to_audio_segment(duration=500) for n in notes2])
sequence3 = sum([Sine(n).to_audio_segment(duration=500) for n in notes3])
# concatenate the sine wave and the sequence
music = sequence

# export the music to a WAV file
sequence.export("Signals/music.wav", format="wav", bitrate="16", parameters=["-ar", "44100"])
sequence1.export("Signals/music1.wav", format="wav", bitrate="16", parameters=["-ar", "44100"])
sequence2.export("Signals/music2.wav", format="wav", bitrate="16", parameters=["-ar", "44100"])
sequence3.export("Signals/music3.wav", format="wav", bitrate="16", parameters=["-ar", "44100"])

