cities = {
    'toronto' : {
        'country' : 'canada',
        'population' : "3 million",
        'fact' : "Toronto is known for the iconic CN Tower.",
        },
    'tokyo' : {
        'country' : 'japan',
        'population' : "14 million",
        'fact' : "Tokyo is the largest metropolitan area in the" +\
                 "world by population.",
        },
    'cairo' : {
        'country' : 'egypt',
        'population' : "10 million",
        'fact' : "Cairo is home to the famous Giza Pyramids",
        } 
    };

cities['new york'] = {
    'country' : 'united states of america',
    'population': '8.5 million',
    'fact': 'Known as "The Big Apple".'  
    };

for city, city_info in cities.items() :
    print("\n" + "Here are few interesting facts about " + 
        city.title() + ":");
    for key, info in city_info.items() :
            if key == 'country' :
                print(key.title() + " : " + info.title());
            else :
                 print(key.title() + " : " + info);
        
