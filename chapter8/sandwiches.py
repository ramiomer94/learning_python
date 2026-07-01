def make_sandwich(*toppings) :
    """ Print the list of toppings that have been requested. """
    print("\nMaking a sandwich with the following toppings: ")
    for topping in toppings :
        print('-' + topping)

make_sandwich('onion')
make_sandwich('cucumber', 'pickels', 'lettuce')
make_sandwich('mayo', 'green olives', 'tomato', 'lettuce')