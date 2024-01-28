import threading
from utilities.userDetails import get_user_details, load_user_details, save_user_details
from utilities.gpt_tools import translate_creole_to_english, interact_with_vivian
from utilities.speech_tools import input_from_voice, speak

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

def main():
    user_details = load_user_details()
    session_just_started = True

    while True:
        if session_just_started:
            if user_details is None or user_details.get('is_new_user', True):
                speak("Welcome! It looks like you're new here.")
                user_details = get_user_details()
                user_details['is_new_user'] = False
                save_user_details(user_details)
            else:
                speak(f"Welcome back! {user_details['name']}")
            session_just_started = False
            speak("Ask me anything and say 'quit' whenever you want to end the chat.")

        creole_input = input_from_voice("", 5)
        print(f'creole_input = {creole_input}')
        if creole_input is None or ('quit' in creole_input.lower()):
            break
        translated_input = translate_creole_to_english(creole_input)
        response = interact_with_vivian(translated_input, user_details, session_just_started)
        speak(response)


if __name__ == "__main__":
    main()
