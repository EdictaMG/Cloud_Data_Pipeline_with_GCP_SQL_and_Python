cities = ['City1', 'City2', 'City3'] #replace City1, City2...with actual city names

# install if needed:
# !pip install sqlalchemy
# !pip install pymysql

# libraries used:
import get_connection_string as gcs
import get_city_data as gcd
import get_population_data as gpd
import get_weather_data as gwd
import get_airport_codes as gac
import get_flight_arrivals as gfa
import pandas as pd
import requests

connection_string = gcs.get_connection_string()

"""## Get_city information"""

city_scraping_df=gcd.get_city_data(cities)

city_pop_scraping_df=gpd.get_population_data(cities)

"""### Countries"""

countries_df = city_scraping_df['country'].unique()
countries_df = pd.DataFrame({"country": countries_df})

countries_df.to_sql('countries',
                  if_exists='append',
                  con=connection_string,
                  index=False)

countries_from_sql = pd.read_sql("countries", con=connection_string)

"""### Cities"""

merged_countries_df = city_scraping_df.merge(countries_from_sql,
                                             on = "country",
                                             how = "left")

cities_df = merged_countries_df.drop(columns=["country"])

cities_df.to_sql('cities',
                  if_exists='append',
                  con=connection_string,
                  index=False)

"""### Population"""

cities_from_sql = pd.read_sql("cities", con=connection_string)

merged_population = cities_from_sql.merge(city_pop_scraping_df,
                                   on = "city",
                                   how="left")

population_df = merged_population[['city_id','population','year']]

population_df.to_sql('population',
                  if_exists='append',
                  con=connection_string,
                  index=False)

population_from_sql = pd.read_sql("population", con=connection_string)

"""### Get_weather"""

cities = cities_from_sql["city"].to_list()

city_weather_df = gwd.get_weather_data(cities)

merged_weather_df = city_weather_df.merge(cities_from_sql,
                                   on = "city",
                                   how="left")

weather_df = merged_weather_df.drop(columns=["city","country_id", "latitude","longitude"])

weather_df['forecast_time']=pd.to_datetime(weather_df['forecast_time'])

weather_df.to_sql('weather',
                  if_exists='append',
                  con=connection_string,
                  index=False)

weather_from_sql = pd.read_sql("weather", con=connection_string)

"""### Get_airports"""

city_latitude = cities_from_sql['latitude'].to_list()
city_longitude = cities_from_sql['longitude'].to_list()

airports_df = gac.get_airport_codes(city_latitude, city_longitude)

merged_airport_df = pd.merge(airports_df, cities_from_sql,
                                   on = ['latitude', 'longitude'],
                                   how="left")

airport_df= merged_airport_df.drop(columns=["latitude", "longitude","city","country_id"])

airport_df.to_sql('airports',
                  if_exists='append',
                  con=connection_string,
                  index=False)

airports_from_sql = pd.read_sql("airports", con=connection_string)

airport_icao = airports_from_sql['icao_code'].to_list()

"""### Get_flights"""

flights_df = gfa.get_flight_arrivals(airport_icao)

merged_flights_df = flights_df.merge(airports_from_sql,
                                   on = "icao_code",
                                   how="left")

flights_df = merged_flights_df.drop(columns=["icao_code","iata_code", "airport_name","city_name", "city_id"])

flights_df['arrival_times']=pd.to_datetime(flights_df['arrival_times'])

flights_df.to_sql('flights',
                   if_exists='append',
                   con=connection_string,
                   index=False)