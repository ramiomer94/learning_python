# Let’s make a module that contains the function make_pizza(). To
# make this module, we’ll remove everything from the file pizza.py except the
# function make_pizza():
def make_pizza(size, *toppings) :
    """ Print the list of toppings that have been requested. """

    print("\nMaking a " + str(size) + 
        "-inch pizza with the following toppings: ")
    for topping in toppings:
        print('-' + topping)