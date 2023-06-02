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
db_connection = mysql.connector.connect(
    host='0.0.0.0',
    user='pi',
    password='raspberry',
    database='API'
)
# Execute the create table query
db_cursor = db_connection.cursor()
db_cursor.execute(create_table_query)

# Extract the relevant data from the JSON response
data = json_api['current']
location_data = json_api['location']

# Prepare the insert query
insert_query = '''
INSERT INTO weather_data (
    location_name,
    region,
    country,
    latitude,
    longitude,
    timezone_id,
    localtime_epoch,
    localtime,
    last_updated_epoch,
    last_updated,
    temp_c,
    temp_f,
    is_day,
    condition_text,
    condition_icon,
    condition_code,
    wind_mph,
    wind_kph,
    wind_degree,
    wind_dir,
    pressure_mb,
    pressure_in,
    precip_mm,
    precip_in,
    humidity,
    cloud,
    feelslike_c,
    feelslike_f,
    vis_km,
    vis_miles,
    uv,
    gust_mph,
    gust_kph
) VALUES (
    %(location_name)s,
    %(region)s,
    %(country)s,
    %(lat)s,
    %(lon)s,
    %(tz_id)s,
    %(localtime_epoch)s,
    %(localtime)s,
    %(last_updated_epoch)s,
    %(last_updated)s,
    %(temp_c)s,
    %(temp_f)s,
    %(is_day)s,
    %(condition_text)s,
    %(condition_icon)s,
    %(condition_code)s,
    %(wind_mph)s,
    %(wind_kph)s,
    %(wind_degree)s,
    %(wind_dir)s,
    %(pressure_mb)s,
    %(pressure_in)s,
    %(precip_mm)s,
    %(precip_in)s,
    %(humidity)s,
    %(cloud)s,
    %(feelslike_c)s,
    %(feelslike_f)s,
    %(vis_km)s,
    %(vis_miles)s,
    %(uv)s,
    %(gust_mph)s,
    %(gust_kph)s)
    # Execute the SQL statement
cursor.execute(sql, values)

# Commit the changes to the database
db.commit()

# Close the cursor and database connection
cursor.close()
db.close()

print("Data saved to MySQL successfully!")
