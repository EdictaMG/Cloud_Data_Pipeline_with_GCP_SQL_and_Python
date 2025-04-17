# Creation of an automated Cloud Data Pipeline using GCP, SQL and Python

Imagine having round-the-clock access to fresh, up-to-date information on a topic you care about—automatically collected, stored in the cloud, and available to anyone you choose. That’s exactly what this project does.

### Situation
In this fictional project for a company called "Gans," the goal was to optimize the availability of e-scooters in highly populated cities with high tourist traffic—especially younger travelers arriving on budget flights. Gans wanted to make sure scooters were available where and when tourists needed them most, like near airports. They also knew weather could significantly impact demand (e.g., rain lowers usage).

To support this goal, I built a fully automated data pipeline using Python, SQL, and Google Cloud Platform (GCP). The pipeline collects:
- **City and population data** from Wikipedia
- **Weather forecasts** using the OpenWeatherMap API
- **Flight arrivals** using the AeroDataBox API

The entire system is automated through the cloud, so once it’s set up, there’s no manual work needed to keep the data flowing.

### Approach
#### Phase 1: Local Pipeline
- Scraped Wikipedia for city data: name, country, population, coordinates.
- Pulled weather forecasts and flight data using APIs.
- Stored all data in a local MySQL database using Python scripts in Jupyter Notebooks.

#### Phase 2: Cloud Automation
- Migrated the pipeline to GCP.
- Scheduled scripts to run automatically using GCP Cloud Functions and Cloud Scheduler.
- Data is saved to a MySQL cloud database (Cloud SQL).
- No need to manage servers—the pipeline runs automatically.

### Learnings
I documented my learning journey in this Medium article:
[Building a Data Pipeline with Python, SQL, and GCP: A Growth Journey](https://medium.com/@edictamg/building-a-data-pipeline-with-python-sql-and-gcp-a-growth-journey-4513774a4e25)

In addition to what I shared in the article, designing efficient connections between the SQL database tables turned out to be a great mental workout—and an important part of making the pipeline work smoothly.

### Files
#### Scripts
##### Functions:
- `get_connection_string.py`: Connect to your MySQL local instance.
- `get_connection_string_GCP.py`: Connect to your MySQL Cloud SQL instance.
- `gans_data_pipeline_sql.py`: Main script to collect and send data to your SQL database (city, country, coordinates, population, weather, airports, flights). 
- `get_population_data.py`: Scrapes city population data and population date stamp.
- `get_population_data_GCP.py`: Scrapes city population data and population date stamp for the Cloud SQL instance.
- `get_city_data.py`: Scrapes latitude, longitude, country.
- `get_weather_data.py`: Pulls forecast data from OpenWeatherMap.
- `get_airport_codes.py`: Finds nearby airport codes using AeroDataBox.
- `get_flight_arrivals.py`: Gets upcoming flight data.
- `standardize_tude.py`: Standardizes coordinates to a uniform format.
- `convert_tude.py`: Converts coordinates to decimal format.
- `extract_year.py`: Pulls year from timestamp.

##### Notebooks:
- `Gans_data_pipeline_sql.ipynb`: Local version of main data pipeline.
- `Gans_data_pipeline_sql_GCP.ipynb`: Cloud version of the pipeline.
- `get_weather_data_GCP.ipynb`, `get_population_data_GCP.ipynb`, `get_flights_data_GCP.ipynb`: GCP-ready codes for cloud functions.

##### SQL Queries:
- `Gans_data_pipeline_tables.sql`: Creates tables for the local MySQL instance.
- `Gans_data_pipeline_GCP.sql`: Creates tables in the MySQL Cloud SQL instance.

#### Documentation
- `Gans_tables_schema`: Diagram showing database structure and relationships.

### Using the files
1. Clone/download this repository.
2. Set up local and cloud MySQL instances.
3. Create accounts and get API keys:
   - OpenWeatherMap
   - AeroDataBox
   - Google Cloud Platform (GCP)
4. Update your credentials in `get_connection_string.py` and `get_connection_string_GCP.py`.
5. Customize `gans_data_pipeline_sql.py` with the cities you're interested in.
6. Insert your API keys in the `get_weather_data.py`, `get_flight_arrivals.py`, and `get_airport_codes.py` scripts.
7. Update your credentials in `get_flights_data_GCP.ipynb`, `get_population_data_GCP.ipynb`, and `get_weather_data_GCP.ipynb`.
8. Run `Gans_data_pipeline_tables.sql` to set up local database tables.
9. Run either `gans_data_pipeline_sql.py` or `Gans_data_pipeline_sql.ipynb` (not both) once to load initial data into local database tables.
10. Run `Gans_data_pipeline_GCP.sql` in your GCP MySQL instance.
11. Run `Gans_data_pipeline_sql_GCP.ipynb` once to load initial data into cloud tables.
12. Set-up cloud functions using contents of the notebooks specific for GCP (`get_flights_data_GCP.ipynb`, `get_population_data_GCP.ipynb` and `get_weather_data_GCP.ipynb`) and deploy.
13. Use GCP Cloud Scheduler to automate regular data updates.
15. Check the database to verify new data is being collected.

### Languages and Libraries Used
- Python (3.10.12)
- Pandas (2.2.2)
- BeautifulSoup (4.13)
- Custom functions

### Tools Used
- Jupyter Notebook
- MySQL Workbench
- Google Cloud Platform

### Accounts Required
- [OpenWeatherMap](https://openweathermap.org/api)
- [AeroDataBox](https://rapidapi.com/aedbx-aedbx/api/aerodatabox/)
- [Google Cloud Platform](https://cloud.google.com/)
