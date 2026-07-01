def city_country(city, country) : 
    location = city  + ', ' + country
    return location.title()

place_to_visit = city_country('toronto', 'canada')
print(place_to_visit)

place_to_visit = city_country('tokyo', 'japan')
print(place_to_visit)

place_to_visit = city_country('cairo', 'egypt')
print(place_to_visit)