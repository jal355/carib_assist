import json

def get_user_details():
    print("Welcome to Vivian, your personal assistant!\n")
    print("To get started, I'll need to know a bit more about you.")
    
    name = input("What is your name? ")
    location = input("What is your current location? (City, Country): ")
    preferences = input("What are some of your interests or preferences? (e.g., hobbies, food, music genres): ")
    dietary_restrictions = input("Do you have any dietary restrictions? (e.g., vegetarian, gluten-free): ")
    
    print("\nThank you! Now I can tailor my responses to suit your needs better.")

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


