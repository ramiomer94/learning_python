requested_toppings = ['mushrooms', 'green peppers', 'extra cheese'];
for requested_topping in requested_toppings :
    if requested_topping == 'green peppers' :
        print("Sorry, we are out of green peppers right now.");
    else :
        print("Adding " + requested_topping);

print("\nFinished making your pizza!");

requested_toppings = []

"""
When the name of a list is used in an if statement,
Python returns True if the list contains at least one item;
an empty list evaluates to False

"""

if requested_toppings :
    for requested_topping in requested_toppings :
        if requested_topping == ' green peppers' :
            print("\nSorry, we are out of green peppers right now.");
        else :
            print("Adding " + requested_topping);
else :
    print("\nAre you sure you want a plain pizza?");

available_toppings = ['mushrooms', 'olives', 'green peppers','pepperoni',
                       'pineapple', 'extra cheese'];

requested_toppings = ['mushrooms', 'french fries', 'extra cheese'];

if requested_toppings:
    for requested_topping in requested_toppings :
        if requested_topping in available_toppings :
            print("Adding " + requested_topping + ".");
        else :
            print("Sorry, we don't have " + requested_topping + ".");
else :
    print("Are you sure you want a plain pizza?");

print("\nFinished making your pizza!");