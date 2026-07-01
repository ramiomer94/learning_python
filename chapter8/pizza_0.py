# If you want a function to accept several different kinds of arguments, the
# parameter that accepts an arbitrary number of arguments must be placed
# last in the function definition. Python matches positional and keyword
# arguments first and then collects any remaining arguments in the final
# parameter.
# For example, if the function needs to take in a size for the pizza, that
# parameter must come before the parameter *toppings:

def make_pizza(size, *toppings) :
    """ Print the list of toppings that have been requested. """

    print("\nMaking a " + str(size) + 
        "-inch pizza with the following toppings: ")
    for topping in toppings:
        print('-' + topping)

# In the function definition, Python stores the first value it receives in
# the parameter size. All other values that come after are stored in the tuple
# toppings. 
make_pizza(12, 'pepperoni')
make_pizza(14, 'mushrooms', 'green peppers', 'extra cheese')