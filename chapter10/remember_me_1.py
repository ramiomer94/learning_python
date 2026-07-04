from pathlib import Path
import json

def get_stored_user_info(path) :
    """ Get stored user information if available. """
    if path.exists() :
        user_info = json.loads(path.read_text())
        return user_info
    else :
        return None

def get_new_user_info(path) :
    """ Prompt for a new name, age, and location. """""
    user_info = {}
    username = input("What is your name? ")
    age = int(input("How old are you? "))
    location = input("Where do you lve? ")

    user_info['name'] = username
    user_info['age'] = age
    user_info['city'] = location

    path.write_text(json.dumps(user_info))

    return user_info


def display_user_info() :
    """ Display the user info. """
    path = Path('user_info.json')
    user_info = get_stored_user_info(path)

    if user_info :
        print(f"Hello {user_info['name'].title()}, " +
            f"you are {user_info['age']} " +
            f"and you live in {user_info['city'].title()}.")
    else :
        user_info = get_new_user_info(path)
        print(f"Hello {user_info['name'].title()}, we got you info.")

display_user_info()

