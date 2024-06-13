# Location detection
import geopy
from geopy.geocoders import Nominatim

# Define a function to find the country for each location
def find_country(location_name):
    try:
        geolocator = Nominatim(user_agent="app", timeout=10)
        location = geolocator.geocode(location_name)
        if location is None:
            return "I'm sorry, I could not find this location!"

        # Use reverse to find the country
        reverse_location = geolocator.reverse((location.latitude, location.longitude), exactly_one=True)
        address = reverse_location.raw['address']
        
        # Extract the country from the address
        country = address.get('country', None)
        if country:
            return country
        else:
            return "I'm sorry, I could not find the country for this location!"
    except geopy.exc.GeocoderTimedOut:
        return "Geocoding service timed out. Please try again."