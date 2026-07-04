from pathlib import Path

filenames = ['cats.txt', 'dogs.txt']
for filename in filenames :
    try :
        print(Path(filename).read_text())
    except FileNotFoundError :
        # print(f"The file {filename} does not exist.")
        pass # fail silently