import requests
from playsound import playsound

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

    #playsound("output.mp3")
                
                 
speak("Welcome to Pittsburgh")