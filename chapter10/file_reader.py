from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text()
contents = contents.rstrip()
print(contents)

# We can strip the trailing newline character when we read the contents
#  of the file, by applying the rstrip() method immediately after calling
# read_text():

# This approach is called method chaining, and you’ll see it used often
# in programming.
contents = path.read_text().rstrip()
print(contents)

# You can use the splitlines() method to turn a long string into a set of
# lines, and then use a for loop to examine each line from a file, one at a
#  time:
lines = path.read_text().splitlines()
for line in lines :
    print(line)


