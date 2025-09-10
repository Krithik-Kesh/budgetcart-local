import googlemaps
import pandas as pd

def turn_miles_to_meters(miles):
  try:
    return miles * 1,609.344
  except:
    return 0

#API STUFF
API_KEY = open('devcontainer.env', 'r').read()
ME = googlemaps.Client(API_KEY)

#USER LOCATION INITIALIZATION AND GOOGLE API STORE FINDER
user_location = (43.647068, -79.390436) #Generic location
search = 'grocery_store'
distance = turn_miles_to_meters(15)
list_of_stores = []

response = ME.places_nearby(
  location = user_location,
  keyword = search,
  name = 'grocery stores',
  radius = distance
)

list_of_stores.extend(response.get('results'))
file = open('../results.txt', 'w')
file.writelines(str(list_of_stores))
