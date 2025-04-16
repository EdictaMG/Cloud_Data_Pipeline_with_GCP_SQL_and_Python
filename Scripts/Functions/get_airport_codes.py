#get city airport codes from AeroDatabox

import pandas as pd
import requests

def get_airport_codes(city_latitude, city_longitude):
    radius = 50 # can change radius to a smaller distance or larger canvas
    limit = 250
    icao_code = []
    iata_code = []
    airport_name = []
    city_name =[]
    latitude = []
    longitude = []

    for lat, lon in zip(city_latitude, city_longitude):
        url = "https://aerodatabox.p.rapidapi.com/airports/search/location"

        querystring = {"lat":f"{lat}",
                       "lon":f"{lon}",
                       "radiusKm":f"{radius}",
                       "limit":f"{limit}",
                       "withFlightInfoOnly":"false"}
        headers = {
            	"x-rapidapi-key": "123abc", #replace "123abc" with your actual API key from AeroDataBox
            	"x-rapidapi-host": "aerodatabox.p.rapidapi.com"
            }
        airport_response = requests.get(url, headers=headers, params=querystring)

        airport_response_json = airport_response.json()

        for i in airport_response_json['items']:
            icao_code.append(i.get('icao', None)), #icao_code
            iata_code.append(i.get('iata', None)), #iata_code
            airport_name.append(i.get('shortName', None)), #airport_name
            city_name.append(i.get('municipalityName')) #city_name
            
        for lat,lon in zip (city_latitude, city_longitude):
            latitude.append(lat) # new 
            longitude.append(lon) # new

        airports = pd.DataFrame(list(zip(icao_code, iata_code, airport_name, city_name, latitude, longitude)),
                                  columns = ['icao_code', 'iata_code', 'airport_name', 'city_name', 'latitude', 'longitude'])

    return(airports)