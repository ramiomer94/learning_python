roro = {
    'kind' : 'dog',
    'owner_name' : 'ali',
    }

fofo = {
    'kind' : 'cat',
    'owner_name' : 'sarah',
    }   

antar = {
    'kind' : 'lizard',
    'owner_name' : 'pat',
}

pets = [roro, fofo, antar];

for pet in pets :
    print("\n" + pet['owner_name'].title() + " owns a pet and it is a " +
        pet['kind']);    