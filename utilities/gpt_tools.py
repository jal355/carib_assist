
import os 
#NOTE: HIDE THIS BEFORE PUBLISHING CODE
os.environ['OPENAI_API_KEY'] = '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'

from openai import OpenAI
client = OpenAI()

def translate_creole_to_english(creole_phrase):
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", 
                 "content": '''You are a translator from Caribbean English-based Creole/Patois to American English.
                               Please provide direct translations only, 
                               without additional context or information.'''},
                {"role": "user", "content": creole_phrase}
            ],
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        
        # Correctly accessing the response
        translated_text = response.choices[0].message.content
        # print(f"~~~~going through translator~ : {translated_text}~~~~~~\n~~~~~~")
        return translated_text
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

#-------------------------------------------------------------------------------
def create_contextual_introduction(user_details):
    intro = "This is a conversation with a user who is "
    if user_details.get("is_new_user", True):
        intro += "new here. "
    else:
        intro += "returning. "

    intro += f"The user's name is {user_details.get('name', 'unknown')}, "
    intro += f"they are located in {user_details.get('location', 'an unknown location')}, "
    intro += f"their interests are {user_details.get('preferences', 'not specified')}, "
    intro += f"and they have {user_details.get('dietary_restrictions', 'no')} dietary restrictions."

    return intro

#-------------------------------------------------------------------------------

def interact_with_vivian(english_phrase, user_details, include_context):
    messages = [
        {"role": "system", "content": "You are a Virtual Assistant named Vivian."}
    ]
    if include_context:
        contextual_intro = create_contextual_introduction(user_details)
        messages.append({"role": "user", "content": contextual_intro})
    
    messages.append({"role": "user", "content": english_phrase})

    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=messages,
            temperature=1,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"An error occurred: {e}")
        return None