# Now we’ll make a separate file called making_pizzas.py in the same
# directory as pizza.py. This file imports the module we just created and then
# makes two calls to make_pizza():

import pizza

pizza.make_pizza(12, 'pepperoni')
pizza.make_pizza(14, 'mushrooms', 'green peppers', 'extra cheese')

# Importing Specific Functions
# You can also import a specific function from a module. Here’s the general
# syntax for this approach:
# from module_name import function_name
# You can import as many functions as you want from a module by separating
#  each function’s name with a comma: 
#           from module_name import function_0, function_1, function_2
# The making_pizzas.py example would look like this if we want to import
# just the function we’re going to use:
#           from pizza import make_pizza

# make_pizza(16, 'pepperoni')
# make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
# With this syntax, you don’t need to use the dot notation when you call a
# function. Because we’ve explicitly imported the function make_pizza() in the
# import statement, we can call it by name when we use the function.