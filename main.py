import numpy as np
import sounddevice as sd
from scipy.io.wavfile import write
import speech_recognition as sr

fs = 44100
seconds = 5

print("🎤 Recording...")
audio = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
sd.wait()

#  FIX: convert to PCM-16
audio = np.int16(audio / np.max(np.abs(audio)) * 32767)

write("voice.wav", fs, audio)

r = sr.Recognizer()
with sr.AudioFile("voice.wav") as source:
    audio_data = r.record(source)

print("⏳ Recognizing...")
print("✅ Text:", r.recognize_google(audio_data))









