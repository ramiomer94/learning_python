from pathlib import Path
import json

def get_stored_number(path) :
    """ Get stored favorite number if available. """
    if path.exists() :
        number = json.loads(path.read_text())
        return number
    else :
        return None

def get_new_number(path) :
    """ Prompt the user for a favorite number. """
    number = input("What is your favorite number? ")
    path.write_text(json.dumps(number))
    return number

def your_favorite_number() :
    """ Reveal the user's favorite number. """
    path = Path('number.json')
    number = get_stored_number(path)
    
    if number :
        print(f"I know your favorite number! It's {number}.")
    else :
        number = get_new_number(path)


your_favorite_number()