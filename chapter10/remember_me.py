from pathlib import Path
import json



# We need to combine the remember_me and greet_user programs into one file.
# When someone runs remember_me.py, we want to retrieve their username from
# memory if possible; if not, we’ll prompt for a username and store it in
# username.json for next time. We could write a try-except block here to
#  respond appropriately if username.json doesn’t exist, but instead we’ll
#  use a handy method from the pathlib module:

# filename = 'username.json'
# path = Path(filename)

# if path.exists() :
#    contents = json.loads(path.read_text())
#    print(f"Welcome back, {contents.title()}")
# else :
#    username = input("What is your name? ")
#    contents = json.dumps(username)
#    path.write_text(contents)
#    print(f"We'll remember you when you come back, {username.title()}!")


# Often, you’ll come to a point where your code will work, but you’ll recognize
# that you could improve the code by breaking it up into a series of functions
# that have specific jobs. This process is called refactoring. Refactoring makes
# your code cleaner, easier to understand, and easier to extend.We can refactor
#  remember_me.py by moving the bulk of its logic into one or more functions.

def get_stored_username(path) :
    """ Get stored username if available. """
    if path.exists() :
        username = json.loads(path.read_text())
        return username
    else :
        None

def get_new_username(path) :
    """ Prompt for a new username. """
    username = input("What is your name? ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user() :
    """ Greet the user by name. """
    path = Path('username.json')
    username = get_stored_username(path)
    if username :
        while True :
            answer = input(f"Are you {username.title()}? (y/n) ")
            if answer == 'y' :
                print(f"Welcome back, {username.title()}")
                break
            elif answer == 'n' :
                username = get_new_username(path)
                print(f"We'll remember you when you come back, " +
                    f"{username.title()}!")
                break
            else :
                print("Invalid input. Only enter 'y' for yes and 'n' for no.")
            
    else :
        username = get_new_username(path)
        print(f"We'll remember you when you come back, {username.title()}!")


greet_user()