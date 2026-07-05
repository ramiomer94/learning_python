from city_functions import get_location_info

def test_city_country() :
    """Do locations like 'Santiago, Chile' work?"""
    location_info = get_location_info('santiago', 'chile')
    assert location_info == 'Santiago, Chile'

def test_city_country_population() :
    """Do locations info like 'Santiago, Chile - population 5000000' work? '"""
    location_info = get_location_info('santiago', 'chile', '5000000')
    assert location_info == 'Santiago, Chile - population 5000000'