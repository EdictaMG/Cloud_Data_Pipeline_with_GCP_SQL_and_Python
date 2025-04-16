import pandas as pd
import requests

def get_flight_arrivals(airport_icao):

  utc_now = pd.Timestamp.utcnow()
  tomorrow = utc_now + pd.Timedelta(hours=24)
  tomorrow_plus_12 = tomorrow + pd.Timedelta(hours=12)

  airlines = []
  flight_numbers = []
  arrival_times = []
  arrival_terminals = []
  all_arrivals = []
  icao_code = []

  for codes in airport_icao:
    url = f"https://aerodatabox.p.rapidapi.com/flights/airports/icao/{codes}/{tomorrow}/{tomorrow_plus_12}"
    querystring = {"direction":"Arrival","withPrivate":"true"}
    headers = {
      "x-rapidapi-key": "123abc", #replace "123abc" with your own API key from AeroDataBox
      "x-rapidapi-host": "aerodatabox.p.rapidapi.com"
    }

    try: 
        arrivals_response = requests.get(url, headers=headers, params=querystring)

        if arrivals_response.status_code == 200:
            arrivals_response_json = arrivals_response.json()

            for i in arrivals_response_json['arrivals']:
                airlines.append(i['airline'].get('name',None))#airline
                flight_numbers.append(i.get('number', None))#flight numbers
                arrival_times.append(i['movement']['scheduledTime'].get('utc', None)) #all arriving flights times
                arrival_terminals.append(i['movement'].get('terminal', None)) #terminals
                icao_code.append(codes)  # append the current ICAO code
            
            for codes in airport_icao:
                icao_code.append(codes)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data for airport code {codes}: {e}")

  if airlines:
      return(pd.DataFrame(list(zip(icao_code, airlines,flight_numbers, arrival_times, arrival_terminals)),
                                  columns = ['icao_code','airlines', 'flight_numbers', 'arrival_times', 'arrival_terminals']))

  else:
      print("No arrivals data collected.")
