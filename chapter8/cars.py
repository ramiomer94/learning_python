def make_car(manufacturer, model, **car_info) :
    """ Build a dictionary containing everything we know about a car. """
    car_profile = {}
    car_profile['manufacturer'] = manufacturer
    car_profile['model'] = model

    for key, value in car_info.items() :
        car_profile[key] = value
    
    return car_profile

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
