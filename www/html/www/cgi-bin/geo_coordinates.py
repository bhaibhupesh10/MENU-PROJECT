#!/usr/bin/env python3

import cgi
import cgitb
import json
from geopy.geocoders import Nominatim

# Enable CGI traceback for debugging
cgitb.enable()

# Print necessary headers
print("Content-Type: application/json\n")

# Parse the query parameters
form = cgi.FieldStorage()
location_name = form.getvalue("location")

# Function to get coordinates
def get_coordinates(location_name):
    geolocator = Nominatim(user_agent="my_geocoder")
    location = geolocator.geocode(location_name)
    if location:
        return {"latitude": location.latitude, "longitude": location.longitude}
    else:
        return {"error": "Location not found"}

# Get coordinates for the provided location
coordinates = get_coordinates(location_name)

# Output the result as JSON
print(json.dumps(coordinates))
