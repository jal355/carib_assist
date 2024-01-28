import threading
import os 
import requests
from playsound import playsound
#NOTE: HIDE THIS BEFORE PUBLISHING CODE
os.environ['OPENAI_API_KEY'] = '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'

from openai import OpenAI
client = OpenAI()
import speech_recognition as sr

from utilities.userDetails import get_user_details, load_user_details, save_user_details
from utilities.gpt_tools import translate_creole_to_english, interact_with_vivian

def input_with_timeout(prompt, timeout):
    print(prompt, end=' ', flush=True)
    result = [None]
    def set_result():
        result[0] = input()
    thread = threading.Thread(target=set_result)
    thread.daemon = True
    thread.start()
    thread.join(timeout)
    if thread.is_alive():
        print("\n\nTime's up! Exiting.")
    return result[0]

def record():
    # obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)  # listen for 1 second to calibrate the energy threshold for ambient noise levels
        audio = r.listen(source)

    # write audio to a WAV file
    with open("results.wav", "wb") as f:
        f.write(audio.get_wav_data())

def transcribe():
    audio_file = open("results.wav", "rb")
    transcript = client.audio.transcriptions.create(
    model="whisper-1", 
    file=audio_file, 
    response_format="text"
    )
    print(transcript)
    return transcript

def speak(output):
    CHUNK_SIZE = 1024
    url = "https://api.elevenlabs.io/v1/text-to-speech/TuLQaI5a4YprYEdpHtqM"

    headers = {
      "Accept": "audio/mpeg",
      "Content-Type": "application/json",
      "xi-api-key": "957ca64486ae940f1cc8b2d48b3f3840"
    }

    data = {
      "text": output,
      "model_id": "eleven_monolingual_v1",
      "voice_settings": {
        "stability": 0.5,
        "similarity_boost": 0.5
      }
    }

    response = requests.post(url, json=data, headers=headers)
    with open('output.mp3', 'wb') as f:
        for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
            if chunk:
                f.write(chunk)   

    playsound("output.mp3")
  

def main():
    user_details = load_user_details()
    session_just_started = True

    while True:
        if session_just_started:
            if user_details is None or user_details.get('is_new_user', True):
                print("Welcome! It looks like you're new here.")
                user_details = get_user_details()
                user_details['is_new_user'] = False
                save_user_details(user_details)
            else:
                print(f"Welcome back! {user_details['name']}")
            session_just_started = False

        record() #records until user stops talking
        creole_input = transcribe() #transcribes input
        if creole_input is None or creole_input.lower() == 'q':
            break

        translated_input = translate_creole_to_english(creole_input)
        response = interact_with_vivian(translated_input, user_details, session_just_started)
        
        print(response)
        speak(response)
    

if __name__ == "__main__":
    main()

