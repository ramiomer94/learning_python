"""A simple class to represent a die"""

from random import randint

class Die() :
    def __init__(self, sides=6) :
        "Initialize the number of sides the die has"
        self.sides = sides
    
    def roll_die(self) :
        """Simulate the roll of a die"""
        print("Rolling a " + str(self.sides) + "-sided die.")
        roll = randint(1,self.sides)
        print("The die landed on " + str(roll) + ".")

six_sided_die = Die()
for roll_number in range(10) :
    print("Roll " + str(roll_number + 1) + ": ")
    six_sided_die.roll_die()

print("\n")
ten_sided_die = Die(10)
for roll_number in range(10) :
    print("Roll " + str(roll_number + 1) + ": ")
    ten_sided_die.roll_die()

print("\n")
twenty_sided_die = Die(20)
for roll_number in range(10) :
    print("Roll " + str(roll_number + 1) + ": ")
    twenty_sided_die.roll_die()