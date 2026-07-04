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

path = Path('pi_million_digits.txt')
contents = path.read_text()
lines = contents.splitlines()
pi_string = ''
for line in lines :
    pi_string += line.lstrip()

print(pi_string[:52])
print(len(pi_string[:52]))

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string :
    print("Your birthday appears in the first million digits of pi!")
else :
    print("Your birthday does not appear in the first million digits of pi.")
