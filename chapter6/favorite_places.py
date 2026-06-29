favorite_places = {
    'mark' : ['paris', 'rome', 'london'],
    'lisa' : ['tokyo', 'seoul'],
    'ali' : ['cairo'],
    'sarah' : ['toronto', 'new york', 'montreal', 'vancouver'],
    }

print("\nHere are my friends' favorite cities:");

for name, cities in favorite_places.items() :
    print("\n" + name.title() + "'s favorite cities:");
    for city in cities:
        print("\t" + city.title());