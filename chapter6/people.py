person_0 = {
    'first' : 'virgil',
    'last' : 'van djik',
    'age' : 33,
    'city' : 'liverpool',
    }

person_1 = {
    'first' : 'mo',
    'last' : 'salah',
    'age' : 33,
    'city' : 'cairo',
    }

person_2 = {
    'first' : 'sergio',
    'last' : 'ramos',
    'age' : 38,
    'city' : 'mexico city',
    }

people = [person_0, person_1, person_2];

for person in people:
    full_name = person['first'] + " " + person['last'];
    age = person['age'];
    city = person['city'];
    print("\nHere are the info of " + person['first'].title() + ":");
    print("\t" + full_name.title());
    print("\t" + str(age));
    print("\t" + city.title());