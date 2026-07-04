from pathlib import Path

filename = 'learning_python.txt'
path = Path(filename)

contents = path.read_text().rstrip()
print(contents)

print()

for line in contents.splitlines() :
    print(line.replace('Python', 'C'))