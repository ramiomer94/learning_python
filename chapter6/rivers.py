rivers = {
    'nile' : 'egypt',
    'amazon' : 'brazi',
    'yangtze' : 'china',
    };

for river_name, country in rivers.items() :
    print("The " + river_name.title() + " runs through " + country.title() +
        ".");

print();
print();

for river_name in rivers.keys() :
    print(river_name.title());

print();
print();

for country in rivers.values() :
    print(country);