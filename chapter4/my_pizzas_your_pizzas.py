my_pizzas = ['pepporoni', 'cheese', 'vegetaraian'];
friends_pizzas = my_pizzas[:];

my_pizzas.append('hawaian');
friends_pizzas.append('chicken');

print("My favorite pizzas are:");
for pizza in my_pizzas:
    print(pizza);

print("\nMy friend’s favorite pizzas are:" )
for pizza in friends_pizzas:
    print(pizza);