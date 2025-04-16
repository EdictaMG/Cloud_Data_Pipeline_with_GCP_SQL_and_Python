# ensure SQL script (in MySQL) has first been run otherwise there will be no database and tables to populate with the acquired data.

# install the following, if needed:
# !pip install sqlalchemy
# !pip install pymysql

#libraries:
import pandas as pd 
import requests
from bs4 import BeautifulSoup
import convert_tude as ct
import standardize_tude as st

def get_city_data (cities_list):
    
    cities_data = []

    for city in cities_list:
      city_data = {}

      #connecting to website
      city = city.replace(' ', '_') #replacing space for "_" in city names composed of two names, i.e. New York
      city_data ["city"] = city #adding city name to dictionnary
      url = f'https://en.wikipedia.org/wiki/{city}' #target website for scraping
      response = requests.get(url)

      #creating soup
      if response.status_code == 200: #checking status code; if ok, proceed.
        soup = BeautifulSoup(response.content, 'html.parser') #creating soup.

      #scraping country name
      country_name = soup.find(class_='infobox-data').get_text() #getting country name for city.
      country_name = country_name.replace('\xa0', '') #this removes the '\xa0' from some country names output
      city_data ["country"] = country_name #sending info to dictionary

      #scraping latitude and longitude
      lat = ct.convert_tude(st.standardize_tude(soup.find(class_='latitude').get_text())) #get latitude and apply "convert()" function
      city_data ["latitude"]= lat #sending info to dictionary

      lon = ct.convert_tude(st.standardize_tude(soup.find(class_='longitude').get_text())) #get longigute and convert.
      city_data ["longitude"] = lon #sending info to dictionary

      cities_data.append(city_data)

    return pd.DataFrame(cities_data)
