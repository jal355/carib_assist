import json
from utilities.speech_tools import speak, record_audio, input_from_voice


def get_user_details():

    speak("Welcome to Vivian, your personal assistant!\n")
    speak("To get started, I'll need to know a bit more about you.")
    
    name = input_from_voice("What is your name?", duration=5)
    location = input_from_voice("What is your current location? (City, Country): ")
    preferences = input_from_voice("What are some of your interests or preferences? (For example: hobbies, food, music genres): ")
    dietary_restrictions = input_from_voice("Do you have any dietary restrictions? (Such as vegetarian or gluten-free): ")
    
    speak("\nThank you! Now I can tailor my responses to suit your needs better.")

    userDetailsDict = {
        "is_new_user" : True,
        "name": name,
        "location": location,
        "preferences": preferences,
        "dietary_restrictions": dietary_restrictions,
    }

    print(userDetailsDict)
    return userDetailsDict

def save_user_details(user_details):
    with open('user_details.json', 'w') as file:
        json.dump(user_details, file)

def load_user_details():
    try:
        with open('user_details.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return None
