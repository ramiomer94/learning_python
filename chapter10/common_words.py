from pathlib import Path

filenames = ['the_secret_of_chimneys.txt', 'the_green_mummy.txt',
        'pride_and_prejudice.txt']

for filename in filenames :
    try :
        count_0 = Path(filename).read_text().lower().count('the')
        count_1 = Path(filename).read_text().lower().count('the ')
    except FileNotFoundError :
        print(f"The file {filename} does not exist.")
    else :
        print(f"\nThe number of occurences of the string 'the' in file " +
            f"{filename} is {count_0}.")
        print(f"The number of occurences of the string 'the ' in file " +
            f"{filename} is {count_1}")
