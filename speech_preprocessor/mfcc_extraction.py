# speech_preprocessor/mfcc_extraction.py

import librosa
import librosa.display
import matplotlib.pyplot as plt
import os

input_file = "speech_preprocessor/audio_samples/sample.wav"
output_dir = "speech_preprocessor/results"
os.makedirs(output_dir, exist_ok=True)

# Load audio
y, sr = librosa.load(input_file)

# Extract MFCCs
mfccs = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=13)

# Plot and save
plt.figure(figsize=(10, 4))
librosa.display.specshow(mfccs, x_axis='time')
plt.colorbar()
plt.title('MFCC')
plt.tight_layout()
plt.savefig(os.path.join(output_dir, "mfcc_plot.png"))

print("✅ MFCC features extracted and saved.")
