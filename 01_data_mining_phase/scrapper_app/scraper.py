import googlemaps
import pandas as pd
from api_keys import GOOGLE_MAPS_API_KEY

def get_coworkings():
    
    # Initialize Google Maps client
    gmaps = googlemaps.Client(key=GOOGLE_MAPS_API_KEY)

    # Search parameters
    location = 'Spain'
    place_type = 'coworking'

    # Initialize lists to store data
    names = []
    addresses = []
    review_scores = []
    latitudes = []
    longitudes = []
    
    # Perform search request
    results = gmaps.places(query=place_type, location=location)

    # Print names, addresses, review scores, latitude, and longitude of found coworkings
    if 'results' in results:
        for place in results['results']:
            name = place['name']
            address = place['formatted_address']
            review_score = place.get('rating', 'No rating')
            latitude = place['geometry']['location']['lat']
            longitude = place['geometry']['location']['lng']
            print(f"Name: {name}, Address: {address}, Review Score: {review_score}, Latitude: {latitude}, Longitude: {longitude}")
    else:
        print("No results found.")

if __name__ == "__scraper__":
    get_coworkings()

