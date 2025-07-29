# speech_preprocessor/generate_sample_audio.py

import numpy as np
from scipy.io.wavfile import write
import os

os.makedirs("audio_samples", exist_ok=True)

samplerate = 16000
duration = 2
frequency = 440.0

t = np.linspace(0., duration, int(samplerate * duration))
audio = 0.8 * np.sin(2. * np.pi * frequency * t)

audio_int16 = np.int16(audio * 32767)
write("speech_preprocessor/audio_samples/sample.wav", samplerate, audio_int16)

print("✅ sample.wav generated in audio_samples/")
