DROP DATABASE IF EXISTS gans_data_pipeline ;

CREATE DATABASE gans_data_pipeline;

USE gans_data_pipeline;

CREATE TABLE countries (
    country_id INT AUTO_INCREMENT,
    country VARCHAR(255) NOT NULL, 
    PRIMARY KEY (country_id)
);

CREATE TABLE cities (
    city_id INT AUTO_INCREMENT, 
    city VARCHAR(255) NOT NULL,
	latitude FLOAT,
    longitude FLOAT,
    country_id INT,
    PRIMARY KEY (city_id),
	FOREIGN KEY (country_id) REFERENCES countries (country_id)
);

CREATE TABLE population (
    population_id INT AUTO_INCREMENT, -- Automatically generated ID for each author
    population INT,
    year INT,
    city_id INT,
    PRIMARY KEY (population_id),
	FOREIGN KEY (city_id) REFERENCES cities (city_id)
);

CREATE TABLE weather (
    weather_id INT AUTO_INCREMENT, -- Automatically generated ID for each author
    forecast_time DATETIME,
    temp_in_c FLOAT,
    temp_feel FLOAT,
    temp_min FLOAT,
    temp_max FLOAT,
    weather_description VARCHAR (255),
    cloudiness_percent INT,
    humidity_percent INT,
    rain_prob_percent INT,
    wind_speed_m_sec FLOAT,
    city_id INT,
    PRIMARY KEY (weather_id),
	FOREIGN KEY (city_id) REFERENCES cities(city_id)
);
CREATE TABLE airports (
    airport_id INT AUTO_INCREMENT,
    icao_code VARCHAR (255),
    iata_code VARCHAR (255),
    airport_name VARCHAR (255),
    city_name VARCHAR (255),
    city_id INT,
    PRIMARY KEY (airport_id),
	FOREIGN KEY (city_id) REFERENCES cities(city_id)
);
CREATE TABLE flights (
    flight_id INT AUTO_INCREMENT,
    airlines VARCHAR (255),
    flight_numbers VARCHAR (255),
    arrival_times DATETIME,
    arrival_terminals VARCHAR (255),
    airport_id INT,
    PRIMARY KEY (flight_id),
	FOREIGN KEY (airport_id) REFERENCES airports (airport_id)
);
