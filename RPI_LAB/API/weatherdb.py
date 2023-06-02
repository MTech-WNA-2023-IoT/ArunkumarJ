import json
import mysql.connector
from urllib.request import urlopen

# Create a user account and obtain an API key from https://www.weatherapi.com
url = "https://api.weatherapi.com/v1/current.json?key=ff20c525398c4d97ae640555232905&q=kollam&aqi=no"

api_page = urlopen(url)
api = api_page.read()
json_api = json.loads(api)

print("Raw Data")
print(json_api)

# Connect to MySQL database
db = mysql.connector.connect(
    host='0.0.0.0',
    user='pi',
    password='raspberry',
    database='API'
)
# Execute the create table query
db_cursor = db.cursor()
# db_cursor.execute(create_table_query)

# Extract the relevant data from the JSON response
current = json_api['current']
location_data = json_api['location']

# Insert the data into the table

sql = """
INSERT INTO `weather_data` (`location_name`, `region`, `country`, `latitude`, `longitude`, `timezone_id`, `localtime_epoch`, `localtime`, `last_updated_epoch`, `last_updated`, `temp_c`, `temp_f`, `is_day`, `condition_text`, `condition_icon`, `condition_code`, `wind_mph`, `wind_kph`, `wind_degree`, `wind_dir`, `pressure_mb`, `pressure_in`, `precip_mm`, `precip_in`, `humidity`, `cloud`, `feelslike_c`, `feelslike_f`, `vis_km`, `vis_miles`, `uv`, `gust_mph`, `gust_kph`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
"""
# Prepare the values for the SQL statement
values = (
    location_data["name"],
    location_data["region"],
    location_data["country"],
    location_data["lat"],
    location_data["lon"],
    location_data["tz_id"],
    location_data["localtime_epoch"],
    location_data["localtime"],
    current["last_updated_epoch"],
    current["last_updated"],
    current["temp_c"],
    current["temp_f"],
    current["is_day"],
    current["condition"]["text"],
    current["condition"]["icon"],
    current["condition"]["code"],
    current["wind_mph"],
    current["wind_kph"],
    current["wind_degree"],
    current["wind_dir"],
    current["pressure_mb"],
    current["pressure_in"],
    current["precip_mm"],
    current["precip_in"],
    current["humidity"],
    current["cloud"],
    current["feelslike_c"],
    current["feelslike_f"],
    current["vis_km"],
    current["vis_miles"],
    current["uv"],
    current["gust_mph"],
    current["gust_kph"]
)

# Execute the SQL statement
db_cursor.execute(sql, values)
# Commit the changes

db.commit()

# Close the connection

db.close()

print("Data saved to MySQL successfully!")
