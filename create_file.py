from datetime import datetime
import pytz

# zones = pytz.all_timezones

# print(zones) 
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder

geolocator = Nominatim(user_agent="nobodyCares")
tf = TimezoneFinder()

coords = geolocator.geocode("Tokyo")
tf = TimezoneFinder()
timezone = tf.timezone_at(lng=coords.longitude, lat=coords.latitude)

print(datetime.now(pytz.timezone(timezone)))
