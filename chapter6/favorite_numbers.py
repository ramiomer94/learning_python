favorite_numbers = {
    'shaq' : [32, 33, 34],
    'kobe' : [8, 24],
    'lebron': [6, 23],
    'steph' : [30],
    'ronaldo' : [7, 9],
    'messi' : [10, 19],
    };

print("Here are a list of people and their favorite numbers:");
for name, numbers in favorite_numbers.items():
    if len(numbers) == 1:
        print("\n" + name.title() + "'s favorite number is :")
        for number in numbers:
            print("\t" + str(number));
    else :
        print("\n" + name.title() + "'s favorite numbers are:");
        for number in numbers:
            print("\t" + str(number));