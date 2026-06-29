"""
When you know you’ll need more than one line to define
a dictionary, press enter after the opening brace. Then indent the next
line one level (four spaces), and write the first key-value pair, followed by
a comma. From this point forward when you press enter, your text editor
should automatically indent all subsequent key-value pairs to match the first
key-value pair

"""
favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
    }
print(favorite_languages);
print("Sarah's favorite language is: " +
    favorite_languages['sarah'].title() +
    ".");

favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'phil' : 'python',
    }


print();
print();


for name, language in favorite_languages.items() :
    print(name.title() + "'s favorite language is " +
        language.title() + ".");

print();
print();

for name in favorite_languages.keys() :
    print(name.title());

"""
Looping through the keys is actually the default behavior when looping
through a dictionary, so this code would have exactly the same output if you
wrote . . .
for name in favorite_languages:
rather than . . .
for name in favorite_languages.keys():

"""
print();
print();

friends = ['phil' , 'sarah'];

for name in favorite_languages.keys() :
    print(name.title());

    if name in friends :
        print(" Hi " + name.title() + ", I see your favorite language is " +
            favorite_languages[name].title() + "!");

if 'erin' not in favorite_languages.keys() :
    print("Erin, please take our poll!");

print();
print();

"""
A dictionary always maintains a clear connection between each key and
its associated value, but you never get the items from a dictionary in any
predictable order. That’s not a problem, because you’ll usually just want
to obtain the correct value associated with each key.
One way to return items in a certain order is to sort the keys as they’re
returned in the for loop. You can use the sorted() function to get a copy of
the keys in order:

"""

for name in sorted(favorite_languages.keys()) :
    print(name.title(), "thank you for taking the poll.");

print();
print();

"""
If you are primarily interested in the values that a dictionary contains,
you can use the values() method to return a list of values without any keys.

"""
for language in favorite_languages.values() : 
    print(language.title());

print();
print();

"""
This approach pulls all the values from the dictionary without checking
for repeats. That might work fine with a small number of values, but in a
poll with a large number of respondents, this would result in a very
repetitive list. To see each language chosen without repetition,
we can use a set. A set is similar to a list except that each item in the set
must be unique:

When you wrap set() around a list that contains duplicate items, Python
identifies the unique items in the list and builds a set from those items. 

"""

for language in set(favorite_languages.values()) :
    print(language.title());

print();
print();

"""
if we were to store each
person’s responses in a list, people could choose more than one favorite
language. When we loop through the dictionary, the value associated with
each person would be a list of languages rather than a single language.
Inside the dictionary’s for loop, we use another for loop to run through
the list of languages associated with each person:

"""
favorite_languages = {
    'jen' : ['python', 'ruby'],
    'sarah' : ['c'],
    'edwards' : ['ruby', 'go'],
    'phil' : ['python', 'haskell'],
    };


for name, languages in favorite_languages.items() :
    if len(languages) > 1 :
        print("\n" + name.title() + "'s favorite languages are: ");
        for language in languages :
            print("\t" + language.title());
    else :
        print("\n" + name.title() + "'s favorite language is: ") 
        for language in languages:
            print("\t" + language.title());
