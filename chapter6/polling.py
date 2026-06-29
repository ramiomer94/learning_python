favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
    }

people_to_poll = ['leo', 'mo', 'edward', 'mark', 'sadio','jen'];

for name in people_to_poll :
    if name in favorite_languages.keys() :
        print(name.title() + ", thank you for taking the poll.");
    else :
        print(name.title() + ", please take the poll.");