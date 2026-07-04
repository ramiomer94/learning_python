from pathlib import Path

def count_words(path) :
    """ Count the approximate number of words in a file. """
    try :
        num_words = len(path.read_text(encoding='utf-8').split())
    except FileNotFoundError :
        print(f"The file {path} doesn't exist.")
    else:
        print(f"The file {path} has about {num_words} words.")


path = Path('alice.txt')
count_words(path)

print("\n\n")

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames :
    count_words(Path(filename))


