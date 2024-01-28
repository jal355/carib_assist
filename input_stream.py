import os 
#NOTE: HIDE THIS BEFORE PUBLISHING CODE
os.environ['OPENAI_API_KEY'] = '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'

from openai import OpenAI
client = OpenAI()

#!/usr/bin/env python3

# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source)  # listen for 1 second to calibrate the energy threshold for ambient noise levels
    print("Say something!")
    audio = r.listen(source)

# write audio to a WAV file
with open("microphone-results.wav", "wb") as f:
    f.write(audio.get_wav_data())


def transcribe(file_name):
    audio_file = open(file_name, "rb")
    transcript = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file, 
    response_format="text"
    )
    return transcript

input = transcribe("microphone-results.wav")
print(input)