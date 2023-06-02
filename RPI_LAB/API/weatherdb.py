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
db_cursor = db_connection.cursor()
# db_cursor.execute(create_table_query)

# Extract the relevant data from the JSON response
data = json_api['current']
location_data = json_api['location']

# Insert the data into the table

sql = """
INSERT INTO `weather_data` (`id`, `location_name`, `region`, `country`, `latitude`, `longitude`, `timezone_id`, `localtime_epoch`, `localtime`, `last_updated_epoch`, `last_updated`, `temp_c`, `temp_f`, `is_day`, `condition_text`, `condition_icon`, `condition_code`, `wind_mph`, `wind_kph`, `wind_degree`, `wind_dir`, `pressure_mb`, `pressure_in`, `precip_mm`, `precip_in`, `humidity`, `cloud`, `feelslike_c`, `feelslike_f`, `vis_km`, `vis_miles`, `uv`, `gust_mph`, `gust_kph`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
"""

# cursor.execute(sql, (json_api['timestamp'], json_api['temperature'], json_api['humidity'], json_api['wind_speed'], json_api['wind_direction'], json_api['pressure'], json_api['cloudiness'], json_api['precipitation']))

# Commit the changes

db.commit()

# Close the connection

db.close()

print("Data saved to MySQL successfully!")
