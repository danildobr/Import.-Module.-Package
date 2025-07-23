from astropy.time import Time
from astropy.coordinates import solar_system_ephemeris, get_body

def calculate_salary():
    print(f'запустился модуль с именем- {__name__}')
    
def distance_earth_mars():
    '''функция расчитывающая расстояние от Земли до Марса на определённую дату и время'''
    t = Time("2025-03-20 00:00:00")
        
    with solar_system_ephemeris.set('jpl'):
       earth = get_body('earth', t)
       mars = get_body('mars', t)
       distance_earth_mars = earth.separation_3d(mars)
    # Выводим расстояние в астрономических единицах (AU) и километрах
    print(f'Единица измерения расстояний в астрономии, в 1 AU = 149 597 870.7 км.')
    print(f"Расстояние от Земли до Марса: {distance_earth_mars.au:.2f} AU")
    print(f"Расстояние от Земли до Марса: {distance_earth_mars.km:.2f} км")
 
