#can use the following code to get list of cities stored in the MySQL database
#cities_from_sql = pd.read_sql("cities", con=connection_string)

#cities = cities_from_sql['city'].to_list()

#cities

import pandas as pd
import requests

def get_weather_data (cities_list):
    city_name = []
    forecast_time =[]
    temp_c=[]
    temp_feels =[]
    temp_min =[]
    temp_max = []
    weather_desc =[]
    cloudiness =[]
    humidity_p =[]
    prob_rain =[]
    wind_speed =[]
    
    #in the "openweather_response line 29, replace [API_KEY_HERE] with your actual API key from OpenWeatherMap
    
    for city in cities_list:
    # this code uses city names only for getting weather information
    # option for using the city's lat/lon instead of names: "https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={APIkey}"
        openweather_response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid=[API_KEY_HERE]&units=metric")
        openweather_response_json = openweather_response.json()
        
        for i in openweather_response_json['list']:
          forecast_time.append(i.get('dt_txt', None)),
          temp_c.append(i['main'].get('temp', None)),
          temp_feels.append(i['main'].get('feels_like', None)),
          temp_min.append(i['main'].get('temp_min', None)),
          temp_max.append(i['main'].get('temp_max', None)),
          weather_desc.append(i['weather'][0].get('main', None)),
          cloudiness.append(i['clouds'].get('all', None)),
          humidity_p.append(i['main'].get('humidity', None)),
          prob_rain.append(int(i.get('pop', None))*100),
          wind_speed.append(i['wind'].get('speed', None)),
          city_name.append(city)
    # creating a dictionnary by joining or "ziping" (zip) the different lists (list), and adding the column labels at the end (columns).
    city_weather_df = (pd.DataFrame(list(zip(city_name, forecast_time,
                                            temp_c, temp_feels, temp_min,
                                            temp_max, weather_desc, cloudiness,
                                            humidity_p, prob_rain, wind_speed)),
                                  columns=["city", "forecast_time",
                                            "temp_in_c", "temp_feel", "temp_min",
                                            "temp_max", "weather_description", "cloudiness_percent",
                                            "humidity_percent", "rain_prob_percent", "wind_speed_m_sec"]))
    return city_weather_df