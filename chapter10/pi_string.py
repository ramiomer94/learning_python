from pathlib import Path

filename = 'pi_digits.txt'
path = Path(filename)

contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for line in lines :
    pi_string += line.lstrip()

print(pi_string)
print(len(pi_string))
