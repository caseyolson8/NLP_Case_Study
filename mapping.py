#geopy imports
from geopy.extra.rate_limiter import RateLimiter
from geopy import Nominatim
import os
import gmaps

gmaps.configure(api_key=os.environ['GOOGLE_API_KEY'])
#geocode for physical address to lat/long lookup
locator = Nominatim(user_agent="myGeocoder")
geocode = RateLimiter(locator.geocode, min_delay_seconds=1)

#create Coordinates column
data['Coordinates'] = data['Location'].apply(geocode)