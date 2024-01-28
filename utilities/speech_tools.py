import os 
import pygame
import sounddevice as sd
import numpy as np
import wave
import requests 
from gtts import gTTS
from openai import OpenAI

#NOTE: HIDE THIS BEFORE PUBLISHING CODE
os.environ['OPENAI_API_KEY'] = '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'

client = OpenAI()

def transcribe_with_whisper(file_name):

    audio_file = open(file_name, "rb")
    transcript_response = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file, 
    response_format="text")

    print(transcript_response)
    return transcript_response


# def speak(text):
#     print(f'\n{text}\n')
#     cwd = os.getcwd()
#     audio_file_path = os.path.join(cwd, 'audios', 'speech.mp3')

#     tts = gTTS(text=text, lang='en')
#     tts.save(audio_file_path)

#     # Initialize pygame and play the audio
#     pygame.mixer.init()
#     pygame.mixer.music.load(audio_file_path)
#     pygame.mixer.music.play()

#     # Wait for the audio to finish playing
#     while pygame.mixer.music.get_busy():
#         pygame.time.Clock().tick(10)

def speak(text):
    CHUNK_SIZE = 1024
    url = "https://api.elevenlabs.io/v1/text-to-speech/TuLQaI5a4YprYEdpHtqM"

    headers = {
      "Accept": "audio/mpeg",
      "Content-Type": "application/json",
      "xi-api-key": "957ca64486ae940f1cc8b2d48b3f3840"
    }

    data = {
      "text": text,
      "model_id": "eleven_monolingual_v1",
      "voice_settings": {
        "stability": 0.5,
        "similarity_boost": 0.5
      }
    }
    
    cwd = os.getcwd()
    audio_file_path = os.path.join(cwd, 'audios', 'speech.mp3')

    response = requests.post(url, json=data, headers=headers)
    with open(audio_file_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:
                f.write(chunk)

    # Initialize pygame and play the audio
    pygame.mixer.init()
    pygame.mixer.music.load(audio_file_path)
    pygame.mixer.music.play()

    # Wait for the audio to finish playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)


def record_audio(duration, filename, samplerate=44100, channels=1, device=0):
    print("Recording...")
    audio_data = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=channels, dtype='int16', device=device)
    sd.wait()  # Wait for the recording to finish
    print("Recording complete.")

    # Save as WAV file
    with wave.open(filename, 'w') as wf:
        wf.setnchannels(channels)
        wf.setsampwidth(2) # 2 bytes per sample for 'int16'
        wf.setframerate(samplerate)
        wf.writeframes(audio_data.tobytes())

    transcription = transcribe_with_whisper(filename)
    return transcription

def input_from_voice(speak_text=None, duration=10):
    if(speak_text):
        speak(speak_text)

    response = record_audio(duration, 'temp.wav')
    #delete wav
    if os.path.exists('temp.wav'):
        os.remove('temp.wav')

    print(f'\nresponse : {response}\n')

    return response