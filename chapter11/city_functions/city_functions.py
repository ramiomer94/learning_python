# def get_location_info(city, country) :
#     """Generate a neatly formatted location address (City, Country)"""
#     location_address = f"{city}, {country}"
#     return location_address.title()

def get_location_info(city, country, population='') :
    """ Generate a neatly formatted location info """
    location_info = f"{city}, {country}"
    location_info = location_info.title()
    if population :
        location_info += f" - population {population}"
    
    return location_info

