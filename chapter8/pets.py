def describe_pet(animal_type, pet_name) :
    """ Display information about a pet """
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('hamster', 'hary')
describe_pet('dog', 'willie')

# A keyword argument is a name-value pair that you pass to a function.
# You directly associate the name and the value within the argument,
# so when you pass the argument to the function, there’s no confusion
# (you won’t end up with a harry named Hamster). Keyword arguments
# free you from having to worry about correctly ordering your arguments
# in the function call, and they clarify the role of each value in the
# function call.

describe_pet(animal_type='hamster', pet_name='harry')

# The order of keyword arguments doesn’t matter because Python knows
# where each value should go. The following two function calls are
# equivalent:
describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

# When writing a function, you can define a default value for each parameter.
# If an argument for a parameter is provided in the function call, Python uses
# the argument value. If not, it uses the parameter’s default value. So when you
# define a default value for a parameter, you can exclude the corresponding 
# argument you’d usually write in the function call. 

# Note that the order of the parameters in the function definition had to be changed.
# Because the default value makes it unnecessary to specify a type of animal as an
# argument, the only argument left in the function call is the pet’s name. Python 
# still interprets this as a positional argument, so if the function is called with
# just a pet’s name, that argument will match up with the first parameter listed
# in the function’s definition. This is the rea- son the first parameter needs to
# be pet_name.

def describe_pet(pet_name, animal_type='dog') :
    """ Display information about a pet """
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")

describe_pet('willie')
describe_pet(animal_type='hamster', pet_name='harry')

# All of the following calls would work for this function:
# A dog named Willie.
describe_pet('willie')
describe_pet(pet_name='willie')
   
# A hamster named Harry.
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')
