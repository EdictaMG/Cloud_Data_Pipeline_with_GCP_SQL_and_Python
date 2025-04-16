import pandas as pd
import requests
from bs4 import BeautifulSoup
import extract_year as ey

# missing feature of appending ('concatenating') a new row at the end of the df when new information is available
# following a sample coding for that

# template:
# new_row = pd.DataFrame({"Name": ["Eve"], "Age": [28]})
# df = pd.concat([df, new_row], ignore_index=True)

# template adapted to specific names:
# new_pop_row = pd.DataFrame({"city": ["city_name"], "population": [updated_population], "year": [year_stamp]})
# cities_population = pd.concat([cities_population, new_pop_row], ignore_index=True)

def get_population_data (cities_list):
    cities_population = []

    for city in cities_list:
      city_population = {}


      #connecting to website
      city_population ["city"] = city #adding city name to dictionnary
      city = city.replace(' ', '_') #replacing space for "_" in city names composed of two names, i.e. New York
      url = f'https://en.wikipedia.org/wiki/{city}' #target website for scraping
      response = requests.get(url)

      #creating soup
      if response.status_code == 200: #checking status code; if ok, proceed.
        soup = BeautifulSoup(response.content, 'html.parser') #creating soup.

        #scraping city population
        pop = soup.find(class_="infobox ib-settlement vcard").find(string="Population").find_next("td").get_text() #getting population information.
        pop = int(pop.replace(",", "")) #removing commas from figure and making it an integer
        city_population ["population"] = pop #sending info to dictionary

        #scraping population timestamp (year)
        yr = ey.extract_year(soup.find(class_="infobox ib-settlement vcard").find(string="Population").next_sibling.get_text())#getting year for population information.
      else:
        print(f"Failed to receive a response from {city}'s page")

      city_population ["year"]= yr #sending info to dictionary


      cities_population.append(city_population)

    return pd.DataFrame(cities_population)