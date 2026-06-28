meal = 'pizza'
print("Is meal == 'pizza' ? I predict True");
print(meal == 'pizza');
print("\nIs meal == 'ice cream' ? I predict False");
print(meal == 'ice cream');
print("\nIs meal == 'Pizza' ? I predict False");
print(meal == 'Pizza');

balance = 100;
print("\nIs balance < 0 ? I predict False");
print(balance < 0);
print("\nIs balance > 0 ? I predict True");
print(balance > 0);
print("\nIs balance != 100 ? I predict False");
print(balance != 100);
print("\nIs balance >= 100 ? I predict True");
print(balance >= 100);
print("\nIs balance <= 50 ? I predict False");
print(balance <= 50);

animal = 'Cat';
print("\nIs animal == 'Cat' ? I predict True");
print(animal == 'Cat');
print("\nIs animal != 'Dog' ? I predict True");
print(animal != 'Dog');
print("\nIs animal == 'cat' ? I predict False");
print(animal == 'cat');
print("\nIs animal.lower() == 'cat' ? I predict True");
print(animal.lower() == 'cat');


price_0 = 10;
price_1 = 100;

print("\nIs price_0 > 0 and price_1 < 1000 ? I predict True");
print(price_0 > 0 and price_1 < 1000);
print("\nIs price_0 > 20 and price_1 < 1000 ? I predict False")
print(price_0 > 20 and price_1 < 1000);
print("\nIs price_0 >= 0 or price_1 < 1000 ? I predict True");
print(price_0 >= 0 or price_1 < 1000);
print("\nIs price_0 < 0 or price_1 > 1000 ? I predict False");
print(price_0 < 0 or price_1 > 1000);

pets = ['cat', 'dog', 'lizard', 'snake'];
print("\nIs cat in the pets list ? I predict true");
print('cat' in pets);
print("\nIs elephant in the pets list ? I predict False")
print('elephant' in pets);
print("\nIs elephant not in the list ? I predict True");
print('elephant' not in pets);
print("\nIs cat not in the pets list ? I predict False");
print('cat' not in pets);